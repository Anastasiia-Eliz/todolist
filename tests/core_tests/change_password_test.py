import pytest


@pytest.mark.django_db
def test_update_password(client):
    """Тест на проверку смены пароля пользователя"""
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
        {'username': 'test', 'password': 'test1234567'},
        content_type='application/json')

    new_password = 'new_password123'

    update_password_response = client.put(
        '/core/update_password',
        {'old_password': user_data['password'], 'new_password': new_password},
        content_type='application/json')

    login_response = client.post(
        '/core/login',
        {'username': 'test', 'password': new_password},
        content_type='application/json')

    assert create_user_response.status_code == 201
    assert login_user_response.status_code == 201
    assert update_password_response.status_code == 200
    assert login_response.status_code == 201
