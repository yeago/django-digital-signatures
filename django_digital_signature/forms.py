from django import forms
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib.auth.hashers import check_password

from django_digital_signature import models as smodels


class SignatureForm(forms.ModelForm):
    document_title = forms.CharField(max_length=255, required=False)
    content_type = forms.IntegerField(required=False, widget=forms.widgets.HiddenInput)
    object_pk = forms.IntegerField(required=False, widget=forms.widgets.HiddenInput)
    password = forms.CharField(max_length=255, widget=forms.widgets.PasswordInput)

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)
        super(SignatureForm, self).__init__(*args, **kwargs)
        if getattr(settings, 'DIGITAL_SIGNATURE_AUTH_TOKEN_NAME', None):
            self.fields['auth_token'].label = settings.DIGITAL_SIGNATURE_AUTH_TOKEN_NAME

    def clean_password(self):
        if not check_password(self.cleaned_data['password'], self._user.password):
            raise forms.ValidationError("Password does not match")
        return self.cleaned_data['password']

    def get_target(self):
        return reverse("apply_signature")

    def save(self, *args, **kwargs):
        record = super(SignatureForm, self).save(commit=False)
        record.user = self._user
        try:
            record.document
        except smodels.Document.DoesNotExist:
            ct = ContentType.objects.get(pk=self.cleaned_data['content_type'])
            record.document = smodels.Document.objects.get_or_create(
                title=self.cleaned_data['document_title'],
                content_type=ct, object_pk=self.cleaned_data['object_pk'])[0]

        record.save()

    class Meta:
        model = smodels.Signatory
        fields = ['auth_token']
