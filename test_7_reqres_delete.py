import requests
import pytest
import allure
import test_3_reqres_post

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Delete Tests')
@allure.title('Successful User Deletion')
@allure.description('Test the DELETE endpoint to verify that a user can be successfully deleted.')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_reqres_user_by_id():
    user_id = test_3_reqres_post.my_id

    with allure.step('Send DELETE request to delete user'):
        response = requests.delete(f'https://reqres.in/api/users/{user_id}')

    with allure.step('Verify status code is 204'):
        assert response.status_code == 204, f"Expected status code 204 but got {response.status_code}"

