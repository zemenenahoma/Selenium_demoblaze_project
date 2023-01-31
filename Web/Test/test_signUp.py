import time

import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Web.Pages.signUp_page import SignUpPage
from Web.base.test_base import TestBases


class TestSignUp(TestBases):
    @allure.description("test valid information")
    # @allure.step("Enter user name as {0}")
    @pytest.mark.sanity
    def test_sign_up(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()
        sign_up.sign_up_user_name("nx@gmail.com")
        sign_up.sign_up_user_password("n1242")
        sign_up.click_sign_up_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")

        assert alt == "Sign up successful."

        self.driver.switch_to.alert.accept()

    @allure.description("test empty user name")
    @pytest.mark.sanity
    def test_sign_up_with_empty_username(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()
        time.sleep(4)
        sign_up.sign_up_user_name(" ")
        time.sleep(4)
        sign_up.sign_up_user_password("7820315429")
        time.sleep(4)
        sign_up.click_sign_up_button()
        time.sleep(4)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")
        assert alt == "This user already exist."
        self.driver.switch_to.alert.accept()

    @allure.description("home page test")
    @pytest.mark.sanity
    def test_sign_up_with_empty_password(self):
        self.driver = super().init()
        sign_up = SignUpPage(self.driver)
        sign_up.sign_up_page()

        sign_up.sign_up_user_name("nahom1221@gmail.com")

        sign_up.sign_up_user_password("")

        sign_up.click_sign_up_button()
