import pytest


@pytest.mark.django_db
def test_delete_user(client):
	"""Тест на проверку удаления пользователя"""
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

	user_delete_response = client.delete(
		'/core/profile',
	)

	assert create_user_response.status_code == 201
	assert login_user_response.status_code == 201
	assert user_delete_response.status_code == 204
