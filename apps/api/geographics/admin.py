from django.contrib import admin

from .models import City, Country, Region, State, SubRegion


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created",
        "modified",
    )
    list_filter = ("created", "modified")
    search_fields = ("name",)


@admin.register(SubRegion)
class SubRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region", "created", "modified")
    list_filter = ("created", "modified", "region")
    search_fields = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "region",
        "subregion",
        "flag",
        "name",
        "iso2",
        "iso3",
        "utc",
        "numeric_code",
        "phone_code",
        "capital",
        "currency",
        "currency_name",
        "currency_symbol",
        "tld",
        "native",
        "created",
        "modified",
    )
    list_filter = ("created", "modified")
    raw_id_fields = ("region", "subregion")
    search_fields = ("name",)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "country",
        "name",
        "state_code",
        "created",
        "modified",
    )
    list_filter = ("created", "modified")
    raw_id_fields = ("country",)
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "modified", "country", "state", "name")
    list_filter = ("created", "modified")
    raw_id_fields = ("country", "state")
    search_fields = ("name",)
