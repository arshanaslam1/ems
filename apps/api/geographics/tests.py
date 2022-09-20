from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.api.core.tests.factories.geographics import setup_geographics
from apps.api.core.tests.factories.users import UserFactory


class GeographicsViewsTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.geographics_id_list = setup_geographics()
        self.client.force_authenticate(self.user)

    def test_region_list(self):
        url = reverse("api:geographics:region-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_region_details(self):
        url = reverse(
            "api:geographics:region-detail",
            args=[self.geographics_id_list["region"][0]],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subregion_list(self):
        url = reverse("api:geographics:subregion-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subregion_details(self):
        url = reverse(
            "api:geographics:subregion-detail",
            args=[self.geographics_id_list["subregion"][0]],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_list(self):
        url = reverse("api:geographics:country-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_details(self):
        url = reverse(
            "api:geographics:country-detail",
            args=[self.geographics_id_list["country"][0]],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_state_list(self):
        url = reverse("api:geographics:state-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_state_details(self):
        url = reverse(
            "api:geographics:state-detail", args=[self.geographics_id_list["state"][0]]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_list(self):
        url = reverse("api:geographics:city-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_city_details(self):
        url = reverse(
            "api:geographics:city-detail", args=[self.geographics_id_list["city"][0]]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
