from django import template
from django_digital_signature import models as smodels
from django_digital_signature import forms as sforms
from django.contrib.contenttypes.models import ContentType

"""
The below line will seem rather strange. I like Bennet's implementation so much
that I'm using it here. Its so abstract that it really transcends django.contrib.comments,
but that's the only place it exists, so I'm stealing it here.
"""

from django.contrib.comments.templatetags.comments import BaseCommentNode as BaseSignatoryNode

register = template.Library()

class SignatoryListNode(BaseSignatoryNode):
	def render(self, context):
		ctype, pk = self.get_target_ctype_pk(context)
		context[self.as_varname] = smodels.Document.objects.filter(content_type=ctype,object_pk=pk)
		return ""

class SignatoryFormNode(BaseSignatoryNode):
	def render(self, context):
		ctype, pk = self.get_target_ctype_pk(context)
		context[self.as_varname] = sforms.SignatureForm(initial={'content_type': ctype.pk, 'object_pk': pk},user=context['user']) 
		return ""

@register.tag
def get_signatories(parser, token):
	return SignatoryListNode.handle_token(parser, token)

@register.tag
def get_signature_form(parser, token):
	return SignatoryFormNode.handle_token(parser, token)

def signatory_check(signatory, obj):
	ct = ContentType.objects.get_for_model(obj.__class__)
	if smodels.Document.objects.filter(signatory__user=signatory,content_type=ct,object_pk=obj.pk).count():
		return True
	
register.filter("has_signed", signatory_check)
