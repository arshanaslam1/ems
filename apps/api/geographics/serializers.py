from rest_framework import serializers

from apps.api.geographics.models import City, Country, Region, State, SubRegion


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class SubRegionSerializer(serializers.ModelSerializer):
    region_name = serializers.StringRelatedField(source="region")

    class Meta:
        model = SubRegion
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    region_name = serializers.StringRelatedField(source="region")
    subregion_name = serializers.StringRelatedField(source="subregion")

    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    country_name = serializers.StringRelatedField(source="country")

    class Meta:
        model = State
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.StringRelatedField(source="country")
    state_name = serializers.StringRelatedField(source="state")

    class Meta:
        model = City
        fields = "__all__"
