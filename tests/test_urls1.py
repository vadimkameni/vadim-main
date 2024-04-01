import unittest
from django.test import Client
from django.urls import reverse

class TestLoginView(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_invalid(self):
        response = self.client.post(reverse('login'), {'username': 'invalid', 'password': 'invalid'})
        self.assertEqual(response.status_code, 200)  # Меняйте, если нужно другой код
        self.assertContains(response, 'Invalid login')

if __name__ == '__main__':
    unittest.main()
