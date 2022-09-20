import factory
from faker import Faker

from apps.users.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.LazyAttribute(lambda x: fake.unique.name())
