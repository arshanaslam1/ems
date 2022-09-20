from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate


class AuthBaseTest(TestCase):
    url_patterns = None
    tested_urls = []
    factory = APIRequestFactory()

    def setUp(self):
        # self.company_user = CompanyUserFactory()
        # self.simple_user = self.company_user.user
        # self.company = self.company_user.company
        # self.company_admin = AdminUserFactory( company=self.company)
        # self.admin_user = self.company_admin.user
        pass

    def do_authenticated_request(self, view, url_pattern, method, user, kwargs):
        factory_method = getattr(self.factory, method)
        request = factory_method(reverse(url_pattern, kwargs=kwargs))
        force_authenticate(request, user)
        return view(request, **kwargs)

    def assert_admin_request(self, view, url_pattern, method, kwargs):
        self.tested_urls.append(url_pattern)
        # first try no user
        response = self.do_authenticated_request(
            view, url_pattern, method, None, kwargs
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # then try simple user
        response = self.do_authenticated_request(
            view, url_pattern, method, self.simple_user, kwargs
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # then try admin
        response = self.do_authenticated_request(
            view, url_pattern, method, self.admin_user, kwargs
        )
        self.assertNotIn(
            response.status_code,
            [status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED],
        )

    # to use this method ensure that the test that checks for coverag
    # e runs at the end of the set of tests by using test_xxx as the test name
    # this works because the default test execution order is alphabetical
    def assert_url_coverage(self):
        for p in self.url_patterns:
            self.assertTrue(p.name in self.tested_urls, p.name + " is not tested")
