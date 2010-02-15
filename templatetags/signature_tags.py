from django import template
from django_digital_signature import models as smodels

"""
The below line will seem rather strange. I like Bennet's implementation so much
that I'm using it here. Its so abstract that it really transcends django.contrib.comments,
but that's the only place it exists, so I'm stealing it here.
"""

from django.contrib.comments.templatetags.comments import BaseCommentNode as BaseSignatoryNode

from coms.core.consumer.models import Followup

register = template.Library()

class SignatoryListNode(BaseSignatoryNode):
	def render(self, context):
		ctype, pk = self.get_target_ctype_pk(context)
		context[self.as_varname] = smodels.Document.objects.filter(content_type=ctype,object_pk=pk)
		return ""

@register.tag
def get_signatories(parser, token):
	return SignatoryListNode.handle_token(parser, token)
