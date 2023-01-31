import pytest
import allure

from Web.Pages.LoginpageObjects import *
from Web.base.test_base import TestBases


class TestLogin(TestBases):
    @pytest.mark.sanity
    @allure.description("test login correctly")
    def test_login(self):
        self.driver = super().init()

        self.lp = LoginPages(self.driver)

        self.lp.click_on_login_text()

        self.lp.set_user_name("zemeneahgcfvho0et06@gmail.com")
        self.lp.set_user_password("nm182551")
        self.lp.click_login()

        assert self.driver.title == "STORE"

    @pytest.mark.sanity
    @allure.description("test login empty user name")
    def test_login_empty_user_name(self):
        self.driver = super().init()

        self.lp = LoginPages(self.driver)

        self.lp.click_on_login_text()

        self.lp.set_user_name("")
        self.lp.set_user_password("nm182551")
        self.lp.click_login()

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")

        assert alt == "Please fill out Username and Password."

        self.driver.switch_to.alert.accept()

    @pytest.mark.sanity
    @allure.description("test login empty user password")
    def test_login_empty_user_password(self):
        self.driver = super().init()

        self.lp = LoginPages(self.driver)

        self.lp.click_on_login_text()

        self.lp.set_user_name("zemeneabinet06@gmail.com")
        self.lp.set_user_password("nm182551")
        self.lp.click_login()

        assert self.driver.title == "STORE"

    @pytest.mark.sanity
    @allure.description("invalid password")
    def test_login_invalid_user_password(self):
        self.driver = super().init()

        self.lp = LoginPages(self.driver)

        self.lp.click_on_login_text()

        self.lp.set_user_name("zemeneabinet06@gmail.com")
        self.lp.set_user_password("pi")
        self.lp.click_login()

        assert self.driver.title == "STORE"

    @pytest.mark.sanity
    @allure.description("invalid password")
    def test_login_invalid_user_name11(self):
        self.driver = super().init()

        self.lp = LoginPages(self.driver)

        self.lp.click_on_login_text()

        self.lp.set_user_name("zemeneabinet06@gmail.com")
        self.lp.set_user_password("pi")
        self.lp.click_login()

        assert self.driver.title == "STORE"
