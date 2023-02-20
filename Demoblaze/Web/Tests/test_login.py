import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Page.page_login import loginPage


class Test_login(Base_test):

    def test_login_correcrt_datas(self):
        driver = self.driver
        login_page = loginPage(driver)
        login_page.open()
        login_page.loginLink()

    def test_enter_lognin_correct_data1(self):
        driver = self.driver
        login_page = loginPage(driver)
        login_page.open()
        login_page.loginLink()
        login_page.enter_login_values("bela", "tsetsu12")
        login_page.login_button()

    def test_click_wellcome_link(self):
        driver = self.driver
        login_page = loginPage(driver)
        login_page.open()
        login_page.loginLink()
        login_page.enter_login_values("bela", "tsetsu12")
        login_page.login_button()
        login_page.welcome_new_link()

    def test_enter_invalid_lognin_value_2(self):
        driver = self.driver
        login_page = loginPage(driver)
        login_page.open()
        login_page.loginLink()
        login_page.enter_login_values("bel", "bela@12456")
        login_page.login_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print(" Error message: ", alt)
        assert alt == 'Wrong password.'
        self.driver.switch_to.alert.accept()
        login_page.click_close_button()


    def test_login_invalid_passwored_datas(self):
        driver = self.driver
        login_page = loginPage(driver)
        login_page.open()
        login_page.loginLink()
        login_page.enter_login_values("bela", "123edsdf")
        login_page.login_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print(" Error message: ", alt)
        assert alt == 'Wrong password.'
        self.driver.switch_to.alert.accept()
        login_page.click_close_button()

    def test_login_both_empty_datas(self):
        driver = self.driver
        login_page = loginPage(driver)
        login_page.open()
        login_page.loginLink()
        login_page.enter_login_values("", "")
        login_page.login_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message: ", alt)
        assert alt == 'Please fill out Username and Password.'
        self.driver.switch_to.alert.accept()
        login_page.click_close_button()







