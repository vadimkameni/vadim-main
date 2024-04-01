from django.test import SimpleTestCase
from django.urls import resolve
from traur2.views import main, suvenir, kontact, registr, vhod, cart, product_detail, product_detail2

class TestUrls(SimpleTestCase):

    def test_accounts_url_resolves(self):
        url = '/accounts/'
        self.assertEqual(resolve(url).func.view_class, None)

    def test_admin_url_resolves(self):
        url = '/admin/'
        self.assertEqual(resolve(url).func, admin.site.urls)
    def test_home_url_resolves(self):
        url = '/'
        self.assertEqual(resolve(url).func, include('traur2.urls'))