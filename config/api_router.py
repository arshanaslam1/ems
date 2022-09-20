from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.users.api.views import UserViewSet


def custom_router():
    if settings.DEBUG:
        return DefaultRouter()
    else:
        return SimpleRouter()


router = custom_router()
router.register("users", UserViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("geographics/", include("apps.api.geographics.urls")),
]
