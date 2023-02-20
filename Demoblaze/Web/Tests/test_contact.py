import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Page.page_contact import ContactPage

class Test_login(Base_test):

    @allure.description('Navigate to contact page correctly')
    def test_ContactPage_click(self):
        driver = self.driver
        contact_page = ContactPage(driver)
        contact_page.open()
        contact_page.ContactLink()

    @allure.description('fills to contact field with  correctly')
    def test_Contact_correcrt_datas(self):
        driver = self.driver
        contact_page = ContactPage(driver)
        contact_page.open()
        contact_page.ContactLink()
        contact_page.enter_contact_values('yeshubel@gmail.com', 'alex', 'hellow world')
        contact_page.Message_send_button()
        contact_page.Alert_accepter()

    @allure.description('fills to contact field with  inncorect datas')
    def test_Contact_incorrecrt_datas(self):
        driver = self.driver
        contact_page = ContactPage(driver)
        contact_page.open()
        contact_page.ContactLink()
        contact_page.enter_contact_values('123fgh', '123', 'hellow world')
        contact_page.Message_send_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Thanks for the message!!'
        self.driver.switch_to.alert.accept()


    @allure.description('fills to contact field with  empty datas')
    def test_Contact_empty_datas(self):
        driver = self.driver
        contact_page = ContactPage(driver)
        contact_page.open()
        contact_page.ContactLink()
        contact_page.enter_contact_values(' ', ' ', ' ')
        contact_page.Message_send_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Thanks for the message!!'
        self.driver.switch_to.alert.accept()


    @allure.description('fills to contact field with  empty user name datas')
    def test_Contact_emptycontact_name_datas(self):
        driver = self.driver
        contact_page = ContactPage(driver)
        contact_page.open()
        contact_page.ContactLink()
        contact_page.enter_contact_values('yeshubel@gmail.com ', ' ', 'hellow world ')
        contact_page.Message_send_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("Error message:  ", alt, "Thanks!!!")
        assert alt == 'Thanks for the message!!'
        self.driver.switch_to.alert.accept()

