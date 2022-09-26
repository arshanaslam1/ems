"""this module providing data upload csv to
 task model by command line and admin panel"""
import csv

import _io
from django.core.management import BaseCommand
from django.utils import timezone

from apps.api.geographics.models import City, Country, Region, State, SubRegion


def country_csv_data_save(csv_file: _io.TextIOWrapper) -> str:
    """take opened csv file and save data in task model"""
    start_t = timezone.now()
    data = csv.DictReader(csv_file, delimiter=",")
    Region.objects.all().delete()
    SubRegion.objects.all().delete()
    Country.objects.all().delete()
    countries = []
    for row in data:
        try:
            name = row["name"].strip().capitalize()
            iso2 = row["iso2"].strip().upper()
            iso3 = row["iso3"].strip().upper()
            numeric_code = row["numeric_code"].strip()
            phone_code = row["phone_code"].strip()
            capital = row["capital"].strip().capitalize()
            currency = row["currency"].strip()
            currency_name = row["currency_name"].strip()
            currency_symbol = row["currency_symbol"].strip()
            tld = row["tld"].strip()
            native = row["native"].strip()
            utc = row["utc"].strip()
            flag = row["emoji"]
            region = row["region"].strip().capitalize()
            subregion = row["subregion"].strip().capitalize()
        except KeyError:
            return (
                "Eroor: Header are must be named as name, iso2,"
                " iso3, numeric_code, phone_code, capital, currency, "
                "currency_name, currency_symbol, tld, native, utc, flag, subregion, and all Columns ara required "
            )
        region_obj, _ = Region.objects.get_or_create(name=region)
        subregion_obj, _ = SubRegion.objects.get_or_create(
            name=subregion, region_id=region_obj.id
        )
        country = Country(
            name=name,
            iso2=iso2,
            iso3=iso3,
            numeric_code=numeric_code,
            phone_code=phone_code,
            capital=capital.strip(),
            currency=currency,
            currency_name=currency_name,
            currency_symbol=currency_symbol,
            tld=tld,
            native=native,
            utc=utc,
            flag=flag,
            region_id=region_obj.id,
            subregion_id=subregion_obj.id,
        )

        if country not in countries:
            countries.append(country)

        if len(countries) > 5000:
            Country.objects.bulk_create(countries)
            countries = []
    if countries:
        Country.objects.bulk_create(countries)
    end_t = timezone.now()
    total_seconds = (end_t - start_t).total_seconds()
    return f"Loading Regions, Subregions and Country from CSV file took: {total_seconds} seconds."


def state_csv_data_save(csv_file: _io.TextIOWrapper) -> str:
    """take opened csv file and save data in task model"""
    start_t = timezone.now()
    data = csv.DictReader(csv_file, delimiter=",")
    State.objects.all().delete()
    states = []
    for row in data:
        try:
            country_name = row["country_name"].strip().capitalize()
            country_iso2 = row["country_code"].strip().upper()
            name = row["name"].strip().capitalize()
            state_code = row["state_code"].strip().upper()
        except KeyError:
            return (
                "Error: Header are must be named as name, country_iso2,"
                " state_code, country_name and all Columns ara required "
            )
        country_obj, _ = Country.objects.get_or_create(
            name=country_name, iso2=country_iso2
        )
        state = State(
            country_id=country_obj.id,
            name=name,
            state_code=state_code,
        )

        if state not in states:
            states.append(state)
        if len(states) > 5000:
            State.objects.bulk_create(states)
            states = []
    if states:
        State.objects.bulk_create(states)
    end_t = timezone.now()
    total_seconds = (end_t - start_t).total_seconds()
    return f"Loading States from CSV file took: {total_seconds} seconds."


def city_csv_data_save(csv_file: _io.TextIOWrapper) -> str:
    """take opened csv file and save data in task model"""
    start_t = timezone.now()
    data = csv.DictReader(csv_file, delimiter=",")
    City.objects.all().delete()
    cites = []
    for row in data:
        try:
            country_name = row["country_name"].strip().capitalize()
            country_iso2 = row["country_code"].strip().upper()
            state_name = row["state_name"].strip().capitalize()
            state_code = row["state_code"].strip().upper()
            name = row["name"].strip().capitalize()
        except KeyError:
            return (
                "Error: Header are must be named as name, country_name,"
                " country_iso2, state_name, state_code, and all Columns ara required "
            )
        country_obj, _ = Country.objects.get_or_create(
            name=country_name, iso2=country_iso2
        )
        state_obj, _ = State.objects.get_or_create(
            name=state_name, state_code=state_code, country_id=country_obj.id
        )
        city = City(
            country_id=country_obj.id,
            state_id=state_obj.id,
            name=name,
        )
        if city not in cites:
            cites.append(city)
        if len(cites) > 5000:
            City.objects.bulk_create(cites)
            cites = []
    if cites:
        City.objects.bulk_create(cites)
    end_t = timezone.now()
    total_seconds = (end_t - start_t).total_seconds()
    return f"Loading Cites from CSV file took: {total_seconds} seconds."


file_name = ["countries.csv", "states.csv", "cities.csv"]
file_path = "apps/api/geographics/management/commands/csv/"


class Command(BaseCommand):
    """this class provide to register module to data upload command"""

    help = "Loading file Geographic Data from CSV."

    def handle(self, *args, **options):
        """take file path and call task cvs to save data"""
        start_t = timezone.now()
        with open(file_path + file_name[0], encoding="utf-8") as csv_file:
            consume_seconds = country_csv_data_save(csv_file)
        self.stdout.write(self.style.SUCCESS(consume_seconds))

        with open(file_path + file_name[1], encoding="utf-8") as csv_file:
            consume_seconds = state_csv_data_save(csv_file)
        self.stdout.write(self.style.SUCCESS(consume_seconds))

        with open(file_path + file_name[2], encoding="utf-8") as csv_file:
            consume_seconds = city_csv_data_save(csv_file)
        self.stdout.write(self.style.SUCCESS(consume_seconds))

        end_t = timezone.now()
        total_seconds = end_t - start_t
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading file Geographic Data from CSV took: Total {total_seconds} seconds."
            )
        )
