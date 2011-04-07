from django.conf.urls.defaults import * 

urlpatterns = patterns('django_digital_signature.views',
	url("^apply-signature/$", "apply_signature", name="apply_signature"),
)
