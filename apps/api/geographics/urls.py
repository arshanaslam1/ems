from apps.api.geographics.views import (
    CityViewSet,
    CountryViewSet,
    RegionViewSet,
    StateViewSet,
    SubRegionViewSet,
)
from config.api_router import custom_router

app_name = "geographics"

router = custom_router()
router.register(r"regions", RegionViewSet, basename="region")
router.register(r"subregions", SubRegionViewSet, basename="subregion")
router.register(r"cities", CityViewSet, basename="city")
router.register(r"states", StateViewSet, basename="state")
router.register(r"countries", CountryViewSet, basename="country")
urlpatterns = router.urls
