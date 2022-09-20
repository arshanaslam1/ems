import factory
from faker import Faker

from apps.api.geographics.models import City, Country, Region, State, SubRegion

fake = Faker()


class RegionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Region

    name = factory.Sequence(lambda n: "region %d" % n)


class SubRegionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SubRegion

    name = factory.Sequence(lambda n: "subregion %d" % n)
    region = factory.SubFactory(RegionFactory)


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    region = factory.SubFactory(RegionFactory)
    subregion = factory.SubFactory(SubRegionFactory)
    name = factory.LazyAttribute(lambda x: fake.country())
    # flag = factory.LazyAttribute(lambda x: fake.unique.flag())
    iso2 = factory.LazyAttribute(lambda x: fake.country_code())
    # iso3 = factory.LazyAttribute(lambda x: fake.unique.iso3())
    # utc = factory.LazyAttribute(lambda x: fake.unique.utc())
    # numeric_code = factory.LazyAttribute(lambda x: fake.unique.numeric_code())
    # phone_code = factory.LazyAttribute(lambda x: fake.unique.phone_code())
    # capital = factory.LazyAttribute(lambda x: fake.unique.capital())
    # currency = factory.LazyAttribute(lambda x: fake.unique.currency())
    # currency_name = factory.LazyAttribute(lambda x: fake.unique.currency_name())
    # currency_symbol = factory.LazyAttribute(lambda x: fake.unique.currency_symbol())
    # tld = factory.LazyAttribute(lambda x: fake.unique.tld())
    # native = factory.LazyAttribute(lambda x: fake.unique.native())


class StateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = State

    country = factory.SubFactory(CountryFactory)
    name = factory.LazyAttribute(lambda x: fake.state())


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    country = factory.SubFactory(CountryFactory)
    state = factory.SubFactory(StateFactory)
    name = factory.LazyAttribute(lambda x: fake.city())


REGIONS = 2
SUBREGIONS = 4
COUNTRIES = 6
STATES = 8
CITIES = 10


def setup_geographics() -> dict:
    geographics_id_list = {
        "region": [],
        "subregion": [],
        "country": [],
        "state": [],
        "city": [],
    }
    for _ in range(REGIONS):
        region = RegionFactory()
        geographics_id_list["region"].append(region.id)
        for _ in range(SUBREGIONS):
            subregion = SubRegionFactory(region=region)
            geographics_id_list["subregion"].append(subregion.id)
            for _ in range(COUNTRIES):
                country = CountryFactory(region=region, subregion=subregion)
                geographics_id_list["country"].append(country.id)
                for _ in range(STATES):
                    state = StateFactory(country=country)
                    geographics_id_list["state"].append(state.id)
                    for _ in range(CITIES):
                        city = CityFactory(country=country, state=state)
                        geographics_id_list["city"].append(city.id)
    return geographics_id_list
