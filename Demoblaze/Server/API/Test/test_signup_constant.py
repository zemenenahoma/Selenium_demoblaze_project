import allure
import requests
from Demoblaze.Server.API.Constant.Signup_constant import RegisterConstants

class Test_Register(RegisterConstants):
    @allure.description('User registered correctly')
    def test_user_signup_correctly(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10


    @allure.description('User registered with exist email')
    def test_user_signup_incorrectly_exist_password(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_exist_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10

    @allure.description('User registered with exist paswerd')
    def test_user_register_incorrectly_with_exist_passwerd(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_exist_username
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
    #
    @allure.description('User registered with capital letter')
    def test_user_register_both_with_exist(self):
            url = RegisterConstants.url_register
            data = RegisterConstants.data_exist_passwored_and_username
            res = requests.post(url, json=data)
            res_data = res.json()
            assert res.status_code == 400
            assert res.elapsed.total_seconds() < 10


    @allure.description('User registered with exist email')
    def test_user_register_incorrectly_with_null_body(self):
        url = RegisterConstants.url_register
        data = {}
        res = requests.post(url, json=data)
        assert res.status_code == 400