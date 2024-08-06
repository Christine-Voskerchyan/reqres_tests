import requests
import pytest
import allure

my_id = 0


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Create Tests')
@allure.title('Create User')
@allure.description('Test the POST endpoint to create a new user and verify the creation with correct response fields.')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_reqres_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    with allure.step('Send POST request to create a new user'):
        response = requests.post(
            'https://reqres.in/api/users',
            json=data
        )

    with allure.step('Verify status code is 201'):
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "name"'):
        assert 'name' in response_data, "Response does not contain 'name'"

    with allure.step('Verify the name in the response'):
        assert response_data['name'] == data[
            'name'], f"Expected name to be '{data['name']}' but got '{response_data['name']}'"

    with allure.step('Verify response contains "job"'):
        assert 'job' in response_data, "Response does not contain 'job'"

    with allure.step('Verify the job in the response'):
        assert response_data['job'] == data[
            'job'], f"Expected job to be '{data['job']}' but got '{response_data['job']}'"

    with allure.step('Verify response contains "id"'):
        assert 'id' in response_data, "Response does not contain 'id'"

    with allure.step('Verify response contains "createdAt"'):
        assert 'createdAt' in response_data, "Response does not contain 'createdAt'"

    with allure.step('Store created user ID'):
        global my_id
        my_id = response_data['id']
        print(f"Created user ID: {my_id}")
