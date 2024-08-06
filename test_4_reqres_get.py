import requests
import pytest
import allure


@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Get Tests')
@allure.title('Get All Users')
@allure.description('Test the GET endpoint to retrieve users from page 2 and verify the structure and content of the response.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_reqres_users():
    with allure.step('Send GET request to retrieve users from page 2'):
        response = requests.get('https://reqres.in/api/users?page=2')

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "page" key'):
        assert 'page' in response_data, 'Response does not contain key "page"'

    with allure.step('Verify response contains "per_page" key'):
        assert 'per_page' in response_data, 'Response does not contain key "per_page"'

    with allure.step('Verify response contains "total" key'):
        assert 'total' in response_data, 'Response does not contain key "total"'

    with allure.step('Verify response contains "total_pages" key'):
        assert 'total_pages' in response_data, 'Response does not contain key "total_pages"'

    with allure.step('Verify response contains "data" key'):
        assert 'data' in response_data, 'Response does not contain key "data"'

    with allure.step('Verify "data" is a list'):
        assert isinstance(response_data['data'], list), '"data" should be a list'

    for user in response_data['data']:
        with allure.step('Verify user contains "id" key'):
            assert 'id' in user, 'User data does not contain key "id"'

        with allure.step('Verify user contains "email" key'):
            assert 'email' in user, 'User data does not contain key "email"'

        with allure.step('Verify user contains "first_name" key'):
            assert 'first_name' in user, 'User data does not contain key "first_name"'

        with allure.step('Verify user contains "last_name" key'):
            assert 'last_name' in user, 'User data does not contain key "last_name"'

        with allure.step('Verify user contains "avatar" key'):
            assert 'avatar' in user, 'User data does not contain key "avatar"'

    with allure.step('Verify response contains "support" key'):
        assert 'support' in response_data, 'Response does not contain key "support"'

    with allure.step('Verify support data contains "url" key'):
        assert 'url' in response_data['support'], 'Support data does not contain key "url"'

    with allure.step('Verify support data contains "text" key'):
        assert 'text' in response_data['support'], 'Support data does not contain key "text"'


@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Get Tests')
@allure.title('Get User by ID')
@allure.description('Test the GET endpoint to retrieve a specific user by ID and verify the user details.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_reqres_user_by_id():
    user_id = 2

    with allure.step('Send GET request to retrieve user by ID'):
        response = requests.get(f'https://reqres.in/api/users/{user_id}')

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "data" key'):
        assert 'data' in response_data, 'Response does not contain key "data"'

    with allure.step('Verify user data contains "id" key'):
        assert 'id' in response_data['data'], 'User data does not contain key "id"'

    with allure.step('Verify user ID matches'):
        assert response_data['data']['id'] == user_id, f'Expected user id {user_id}, got {response_data["data"]["id"]}'

    with allure.step('Verify user data contains "email" key'):
        assert 'email' in response_data['data'], 'User data does not contain key "email"'

    with allure.step('Verify email matches'):
        assert response_data['data'][
                   'email'] == 'janet.weaver@reqres.in', f'Expected email "janet.weaver@reqres.in", got {response_data["data"]["email"]}'

    with allure.step('Verify user data contains "first_name" key'):
        assert 'first_name' in response_data['data'], 'User data does not contain key "first_name"'

    with allure.step('Verify first name matches'):
        assert response_data['data'][
                   'first_name'] == 'Janet', f'Expected first name "Janet", got {response_data["data"]["first_name"]}'

    with allure.step('Verify user data contains "last_name" key'):
        assert 'last_name' in response_data['data'], 'User data does not contain key "last_name"'

    with allure.step('Verify last name matches'):
        assert response_data['data'][
                   'last_name'] == 'Weaver', f'Expected last name "Weaver", got {response_data["data"]["last_name"]}'

    with allure.step('Verify user data contains "avatar" key'):
        assert 'avatar' in response_data['data'], 'User data does not contain key "avatar"'

    with allure.step('Verify avatar URL matches'):
        assert response_data['data'][
                   'avatar'] == 'https://reqres.in/img/faces/2-image.jpg', f'Expected avatar URL "https://reqres.in/img/faces/2-image.jpg", got {response_data["data"]["avatar"]}'

    with allure.step('Verify response contains "support" key'):
        assert 'support' in response_data, 'Response does not contain key "support"'

    with allure.step('Verify support data contains "url" key'):
        assert 'url' in response_data['support'], 'Support data does not contain key "url"'

    with allure.step('Verify support URL matches'):
        assert response_data['support'][
                   'url'] == 'https://reqres.in/#support-heading', f'Expected support URL "https://reqres.in/#support-heading", got {response_data["support"]["url"]}'

    with allure.step('Verify support data contains "text" key'):
        assert 'text' in response_data['support'], 'Support data does not contain key "text"'

    with allure.step('Verify support text matches'):
        assert response_data['support'][
                   'text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!', f'Expected support text "To keep ReqRes free, contributions towards server costs are appreciated!", got {response_data["support"]["text"]}'


@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Get Tests')
@allure.title('User Not Found')
@allure.description(
    'Test the GET endpoint to ensure that requesting a non-existent user ID returns a 404 status code and an empty response body.')
@allure.severity(allure.severity_level.NORMAL)
def test_user_not_found():
    user_id = 23

    with allure.step('Send GET request for non-existent user ID'):
        response = requests.get(f'https://reqres.in/api/users/{user_id}')

    with allure.step('Verify status code is 404'):
        assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

    with allure.step('Verify response body is empty'):
        assert response.text == '{}', "Response body should be '{}' for a 404 error"

