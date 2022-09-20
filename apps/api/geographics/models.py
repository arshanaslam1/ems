from django.db import models
from django_extensions.db.models import TimeStampedModel


class Region(TimeStampedModel):
    name = models.CharField(unique=True, null=True, blank=True, max_length=255)

    def __str__(self):
        return self.name


class SubRegion(TimeStampedModel):
    name = models.CharField(null=True, blank=True, max_length=255)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subregion",
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (
            "region",
            "name",
        )


class Country(TimeStampedModel):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="region_country",
    )
    subregion = models.ForeignKey(
        SubRegion,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subregion_country",
    )
    flag = models.CharField(null=True, blank=True, max_length=50)
    name = models.CharField(null=True, blank=True, max_length=255)
    iso2 = models.CharField(max_length=10, null=True, blank=True)
    iso3 = models.CharField(max_length=10, null=True, blank=True)
    utc = models.CharField(max_length=10, null=True, blank=True)
    numeric_code = models.CharField(max_length=10, null=True, blank=True)
    phone_code = models.CharField(max_length=20, null=True, blank=True)
    capital = models.CharField(max_length=20, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    currency_name = models.CharField(max_length=50, null=True, blank=True)
    currency_symbol = models.TextField(null=True, blank=True)
    tld = models.CharField(max_length=5, null=True, blank=True)
    native = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (
            "region",
            "subregion",
            "name",
            "iso2",
            "iso3",
        )


class State(TimeStampedModel):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="country_states",
    )
    name = models.CharField(null=True, blank=True, max_length=255)
    state_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (
            "country",
            "name",
            "state_code",
        )


class City(TimeStampedModel):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="country_cites",
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="state_cites",
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
