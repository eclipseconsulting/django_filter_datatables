from factory import DjangoModelFactory, lazy_attribute
from faker import Faker
from faker.providers import person, address, phone_number

from .. import models

fake = Faker()
fake.add_provider(person)
fake.add_provider(address)
fake.add_provider(phone_number)


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = models.Customer

    first_name = lazy_attribute(lambda x: fake.first_name())
    last_name = lazy_attribute(lambda x: fake.last_name())
    city = lazy_attribute(lambda x: fake.city())
    state = lazy_attribute(lambda x: fake.state())
    zip = lazy_attribute(lambda x: fake.zipcode_plus4())
    phone = lazy_attribute(lambda x: fake.phone_number())
