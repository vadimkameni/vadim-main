from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):
    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_registr_view(self):
        response = self.client.get(reverse('registr'))
        self.assertEqual(response.status_code, 200)

    def test_suvenir_view(self):
        response = self.client.get(reverse('suvenir'))
        self.assertEqual(response.status_code, 200)

    def test_kontact_view(self):
        response = self.client.get(reverse('kontact'))
        self.assertEqual(response.status_code, 200)

    def test_vhod_view(self):
        response = self.client.get(reverse('vhod'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail2_view(self):
        response = self.client.get(reverse('product_detail2'))
        self.assertEqual(response.status_code, 200)

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('main'))

    def test_register_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertRedirects(response, reverse('login'))
