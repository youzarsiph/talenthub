""" URLConf for talenthub.industries """

from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)

sub_router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path("", include(router.urls)),
]
