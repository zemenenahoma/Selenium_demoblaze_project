from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Page.page_sign_up import SignUp_Page


class Test_signup(Base_test):

    @allure.description('Navigate to signup page correctly')
    @pytest.mark.sanity
    def test_click_on_signup_page(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        signup.open()
        signup.signup_pagelink()

    @allure.description('sign_up correctly')
    @pytest.mark.sanity
    def test_sign_up_old_correctly(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        signup.open()
        signup.signup_pagelink()
        signup.eneter_signup_values('bela', 'testsu12')
        signup.click_signup_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == "This user already exist."
        self.driver.switch_to.alert.accept()
    @allure.description('sign_up with empty user name and passwored')
    @pytest.mark.sanity
    def test_sign_up_empty_usernameAndpasswored(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        signup.open()
        signup.signup_pagelink()
        signup.eneter_signup_values('', '')
        signup.click_signup_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Please fill out Username and Password.'
        self.driver.switch_to.alert.accept()

    @allure.description('sign_up with empty user name')
    @pytest.mark.sanity
    def test_sign_up_empty_username(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        signup.open()
        signup.signup_pagelink()
        signup.eneter_signup_values(' ', ' tsetsu12')
        signup.click_signup_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'This user already exist.'
        self.driver.switch_to.alert.accept()

    def test_sign_up_empty_passwored(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        signup.open()
        signup.signup_pagelink()
        signup.eneter_signup_values('hana', '')
        signup.click_signup_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Please fill out Username and Password.'
        self.driver.switch_to.alert.accept()

    @allure.description('sign_up empty passwored')
    @pytest.mark.sanity
    def test_sign_new_passwored_and_username(self):
        driver = self.driver
        signup = SignUp_Page(driver)
        signup.open()
        signup.signup_pagelink()
        signup.eneter_signup_values('nahom', ' nahu123')
        signup.click_signup_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")
        assert alt == 'This user already exist.'
        self.driver.switch_to.alert.accept()


