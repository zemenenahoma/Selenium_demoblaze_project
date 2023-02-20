import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Page.page_home import HomePage
import allure

class Test(Base_test):
    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_cart_link_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.CartLink()

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_order_button_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.CartLink()
        login_page.OrederPlace_button()

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_field_valied_datas(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.CartLink()
        login_page.OrederPlace_button()
        login_page.enter_cart_field_values('Alex', 'Israel', 'TelAviv', '1234567', 'June', '2023')
        login_page.PurchaseButton()
        alt = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]").text
        assert alt == "Thank you for your purchase!"

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_field_empty_username(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.CartLink()
        login_page.OrederPlace_button()
        login_page.enter_cart_field_values('', 'Israel', 'TelAviv', '1234567', 'June', '2023')
        login_page.PurchaseButton()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Please fill out Name and Creditcard.'
        self.driver.switch_to.alert.accept()


    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_field_empty_credit_card(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.CartLink()
        login_page.OrederPlace_button()
        login_page.enter_cart_field_values('Alex', 'Israel', 'TelAviv', '', 'June', '2023')
        login_page.PurchaseButton()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Please fill out Name and Creditcard.'
        self.driver.switch_to.alert.accept()