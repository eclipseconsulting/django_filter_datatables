from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from test_plus import TestCase

from apps.customers.models import Customer


class TestCustomer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.add_customer = Permission.objects.get(
            content_type__model='customer', codename='add_customer'
        )

        cls.user = get_user_model().objects.create_user(username='test_user', email='', password='password')
        cls.user.user_permissions.add(cls.add_customer)

    def test_add_customer(self):
        self.assertTrue(self.user.has_perm('customers.add_customer'))
        with self.login(username=self.user, password='password'):
            response = self.get('customers:customer_create')
            self.response_200(response)

            response = self.post('customers:customer_create', data={'name': 'test'})
            self.response_302(response)
            customers = Customer.objects.all()
            self.assertEqual(len(customers), 1)
