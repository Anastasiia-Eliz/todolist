import pytest


@pytest.mark.django_db
def test_login(client):
    """Тест на проверку входа (login)  пользователя"""
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

    login_user_response = client.post(
        '/core/login',
        {'username': user_data['username'], 'password': user_data['password']},
        content_type='application/json')

    assert create_user_response.status_code == 201
    assert login_user_response.status_code == 200
