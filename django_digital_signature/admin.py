from django import forms
from django.contrib import admin
from django.conf import settings
from django_digital_signature import models as smodels


class SignatoryAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignatoryAdminForm, self).__init__(*args, **kwargs)
        if hasattr(settings, 'DIGITAL_SIGNATURE_AUTH_TOKEN_NAME'):
            self.fields['auth_token'].label = settings.DIGITAL_SIGNATURE_AUTH_TOKEN_NAME

    class Meta:
        model = smodels.Document
        fields = '__all__'


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content_object', 'date_created')


class SignatoryAdmin(admin.ModelAdmin):
    list_display = ('document', 'user', 'date_signed')
    form = SignatoryAdminForm

admin.site.register(smodels.Signatory, SignatoryAdmin)
admin.site.register(smodels.Document, DocumentAdmin)
