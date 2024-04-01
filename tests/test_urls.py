from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import main, suvenir, kontact, registr, vhod, cart, product_detail, product_detail2

class TestUrls(SimpleTestCase):

    def test_main_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, main)

    def test_suvenir_url_resolves(self):
        url = reverse('suvenir')
        self.assertEqual(resolve(url).func, suvenir)

    def test_kontact_url_resolves(self):
        url = reverse('kontact')
        self.assertEqual(resolve(url).func, kontact)

    def test_registr_url_resolves(self):
        url = reverse('registr')
        self.assertEqual(resolve(url).func, registr)

    def test_vhod_url_resolves(self):
        url = reverse('vhod')
        self.assertEqual(resolve(url).func, vhod)

    def test_cart_url_resolves(self):
        url = reverse('cart')
        self.assertEqual(resolve(url).func, cart)

    def test_product_detail_url_resolves(self):
        url = reverse('product_detail')
        self.assertEqual(resolve(url).func, product_detail)

    def test_product_detail2_url_resolves(self):
        url = reverse('product_detail2')
        self.assertEqual(resolve(url).func, product_detail2)