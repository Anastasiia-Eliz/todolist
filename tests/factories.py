import factory.django
from factory import Faker

from core.models import User
from goals.models.models import Board, GoalCategory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'test'
    first_name = 'Test'
    last_name = 'Test'
    email = 'test@mail.ru'
    password = 'test1234567'


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = Faker('sentence')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    title = Faker('sentence')
    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)

