from django.conf.urls import patterns, url

urlpatterns = patterns('django_digital_signature.views',
    url("^apply-signature/$", "apply_signature", name="apply_signature"),
)
