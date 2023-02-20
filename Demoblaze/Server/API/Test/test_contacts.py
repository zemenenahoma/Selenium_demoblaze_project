import requests
import allure
from Demoblaze.Server.API.Constant.Contact_constant import HomeConstant

class Test_Register():

    @allure.description('User Contact correctly')
    def test_user_contact_insert_correctly(self):
        URL = HomeConstant.URL
        data = HomeConstant.data_valid
        res = requests.post(URL, json=data)

        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data[HomeConstant.success_key] == True
        assert res_data[HomeConstant.message_key] == 'user insert successfully'

    @allure.description('User registered with exist email')
    def test_user_register_incorrectly_with_exist_email(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_invalid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[RegisterConstants.success_key] == False
        assert res_data[RegisterConstants.message_key] == "user with that email already exists"

    def test_user_register_incorrectly_with_null_body(self):
        url = RegisterConstants.url_register
        data = {}
        res = requests.post(url, json=data)
        assert res.status_code == 400