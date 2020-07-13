from django_digital_signature.forms import SignatureForm
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib import messages

def apply_signature(request,return_url="/",success_msg="Digital signature has been applied"):
	form = SignatureForm(request.POST or None,user=request.user)
	if form.is_valid():
		form.save()
		messages.success(request,success_msg)
	else:
		messages.error(request,"Signature not applied.")
		
	return redirect(request.GET.get("return_url","/"))
