import time
import allure
from selenium.webdriver.common.by import By
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Locators.locators_login import Login_locators


class loginPage(Base_test, Login_locators):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        super().init()

    @allure.step
    @allure.description('Navigate to login page')
    def loginLink(self):
        self.driver.find_element(By.XPATH, self.Login_link).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Insert log in username')
    def eneter_username(self, username):
        self.driver.find_element(By.XPATH, self.LOGIN_username).clear()
        self.driver.find_element(By.XPATH, self.LOGIN_username).send_keys(username)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Insert log in passwored')
    def enter_passwored(self, passwored):
        self.driver.find_element(By.XPATH, self.Login_Passwored).clear()
        self.driver.find_element(By.XPATH, self.Login_Passwored).send_keys(passwored)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('Click login button')
    def login_button(self):
        self.driver.find_element(By.XPATH, self.Login_button).click()
        self.driver.implicitly_wait(5)

    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.Close_button).click()
        self.driver.implicitly_wait(5)

    def welcome_new_link(self):
        time.sleep(3)
        return self.driver.find_element(By.XPATH, self.Wellcome_link).click()

    def logOut_button(self):
        self.driver.find_element(By.XPATH, self.LogOut_link).click()
        self.driver.implicitly_wait(5)

    def Alert_accepter(self):
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(5)

    def enter_login_values(self, UserName, Passwored, ):
        self.eneter_username(UserName)
        self.enter_passwored(Passwored)

