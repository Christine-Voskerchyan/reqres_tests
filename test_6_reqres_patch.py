import requests
import pytest
import allure
import test_3_reqres_post


@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Patch Tests')
@allure.title('Partial Update User Details')
@allure.description('Test the PATCH endpoint to verify that partial updates to user details are applied successfully.')
@allure.severity(allure.severity_level.NORMAL)
def test_reqres_partial_update():
    user_id = test_3_reqres_post.my_id
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step('Send PATCH request to update user details'):
        response = requests.patch(
            f'https://reqres.in/api/users/{user_id}',
            json=data,
        )

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "name" field'):
        assert 'name' in response_data, "Response does not contain 'name'"

    with allure.step('Verify the name has been updated'):
        assert response_data['name'] == data[
            'name'], f"Expected name to be '{data['name']}' but got '{response_data['name']}'"

    with allure.step('Verify response contains "job" field'):
        assert 'job' in response_data, "Response does not contain 'job'"

    with allure.step('Verify the job has been updated'):
        assert response_data['job'] == data[
            'job'], f"Expected job to be '{data['job']}' but got '{response_data['job']}'"

    with allure.step('Verify response contains "updatedAt" field'):
        assert 'updatedAt' in response_data, "Response does not contain 'updatedAt'"


