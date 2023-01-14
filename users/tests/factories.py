from factory.django import DjangoModelFactory
from factory import Faker, SubFactory

from users.models import AuthUser, NormalUser, PremiumPlan, SuperAdmin

class PremiumPlanFactory(DjangoModelFactory):
    class Meta:
        model = PremiumPlan

class AuthUserFactory(DjangoModelFactory):
    email = Faker('email')
    role = AuthUser.NORMAL_USER

    class Meta:
        model = AuthUser

class NormalUserFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    role = AuthUser.NORMAL_USER
    premium_plan = SubFactory(PremiumPlanFactory)

    class Meta:
        model = NormalUser

class SuperAdminFactory(DjangoModelFactory):
    email = Faker('email')
    role = AuthUser.SUPER_ADMIN

    class Meta:
        model = SuperAdmin