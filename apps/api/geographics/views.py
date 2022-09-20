from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.api.geographics.models import City, Country, Region, State, SubRegion
from apps.api.geographics.serializers import (
    CitySerializer,
    CountrySerializer,
    RegionSerializer,
    StateSerializer,
    SubRegionSerializer,
)


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple Read Only ViewSet for viewing Countries.
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "id",
        "name",
    )


class SubRegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple Read Only ViewSet for viewing Countries.
    """

    queryset = SubRegion.objects.all()
    serializer_class = SubRegionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "id",
        "name",
        "region",
    )


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple Read Only ViewSet for viewing Countries.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "id",
        "name",
        "iso2",
        "iso3",
        "utc",
        "phone_code",
        "currency",
        "region",
        "subregion",
    )


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple Read Only ViewSet for viewing States.
    """

    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "id",
        "name",
        "state_code",
        "country",
    )


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple Read Only ViewSet for viewing Cities.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "id",
        "name",
        "state",
        "country",
    )
