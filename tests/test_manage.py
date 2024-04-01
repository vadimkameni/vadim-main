from django.test import TestCase
from myapp.models import MyModel

class MyModelTestCase(TestCase):
    def test_my_model_str_method(self):
        my_model = MyModel(name='Test Model')
        self.assertEqual(str(my_model), 'Test Model')
