import requests
import pytest
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Login Tests')
@allure.title('Successful Login')
@allure.description('Test the POST endpoint for login with valid credentials and verify that a token is returned.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_successful_login():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    with allure.step('Send POST request for successful login'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=data,
        )

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "token" field'):
        assert 'token' in response_data, "Response does not contain 'token'"

    with allure.step('Verify token is not empty'):
        assert len(response_data['token']) > 0, "Token shouldn't be empty"


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Login Tests')
@allure.title('Unsuccessful Login')
@allure.description(
    'Test the POST endpoint for login with missing password and verify that the appropriate error message is returned.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_unsuccessful_login():
    data = {
        "email": "peter@klaven"
    }

    with allure.step('Send POST request for unsuccessful login'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=data,
        )

    with allure.step('Verify status code is 400'):
        assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "error" field'):
        assert 'error' in response_data, "Response does not contain 'error'"

    with allure.step('Verify error message is "Missing password"'):
        assert response_data['error'] == "Missing password", "Error message does not match"

