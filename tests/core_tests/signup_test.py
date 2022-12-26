import pytest

from core.models import User


@pytest.mark.django_db

def test_sign_up(client):
    """Тест на проверку регистрации пользователя"""
    user_data = {
        'username': 'test',
        'first_name': 'Test',
        'last_name': 'Test',
        'email': 'test@mail.ru',
        'password': 'test1234567',
        'password_repeat': 'test1234567'
    }

    create_user_response = client.post(
        '/core/signup',
        data=user_data,
        content_type='application/json')

    user = User.objects.filter(username=user_data['username']).first()

    assert create_user_response.status_code == 201
    assert user.username == user_data['username']

