import time
import allure
import pytest
from selenium.webdriver.common.by import By
from Demoblaze.Web.Base.Base_test import Base_test


from Demoblaze.Web.Locators.locators_SignUp import Signup_locators


class SignUp_Page(Base_test, Signup_locators):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        super().init()

    @allure.description('clicking on signup button - should navigate to signup page')
    @pytest.mark.sanity
    def signup_pagelink(self):
        self.driver.find_element(By.XPATH, self.SignUp_click_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('insert value to "username" input')
    @pytest.mark.sanity
    def enter_Username(self, Username):
        field = self.driver.find_element(By.XPATH, self.UserName_signup_field)
        field.clear()
        field.send_keys(Username)
        self.driver.implicitly_wait(5)

    @allure.description('insert value to "password"')
    @pytest.mark.sanity
    def enter_passwored(self, passwored):
        field = self.driver.find_element(By.XPATH, self.Passwored_signup_field)
        field.clear()
        field.send_keys(passwored)
        self.driver.implicitly_wait(5)

    def Alert_accepter(self):
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(5)

    @allure.description('clicking on signup button')
    @pytest.mark.sanity
    def click_signup_button(self):
        self.driver.find_element(By.XPATH, self.SignUp_button).click()
        self.driver.implicitly_wait(5)

    @allure.description('clicking on signup button')
    @pytest.mark.sanity
    def eneter_signup_values(self, UserName, Passwored):
        self.enter_Username(UserName)
        self.enter_passwored(Passwored)
        self.driver.implicitly_wait(5)

    @allure.description('clicking on signup button')
    @pytest.mark.sanity
    def close_button_click(self):
        self.driver.find_element(By.XPATH, self.Close_signup_close_button).click()
        self.driver.implicitly_wait(5)
