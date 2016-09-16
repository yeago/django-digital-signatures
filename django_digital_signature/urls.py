from django.conf.urls import url
from django_digital_signature.views import apply_signature

urlpatterns = [
    url("^apply-signature/$", apply_signature, name="apply_signature"),
]
