import time
import allure
from selenium.webdriver.common.by import By
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Locators.locators_contact import Contact_locatrors


class ContactPage(Base_test, Contact_locatrors):


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        super().init()

    @allure.step
    @allure.description('clicking on ContactLink- should navigate to Contact page')
    def ContactLink(self):
        self.driver.find_element(By.XPATH, self.Contact_link).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('insert value to "email" input')
    def enter_ContactEmail(self, ContactEmail):
        field = self.driver.find_element(By.XPATH, self.Contact_email_field)
        field.clear()
        field.send_keys(ContactEmail)
        self.driver.implicitly_wait(5)


    @allure.step
    @allure.description('insert value to "contactName" input')
    def enter_ContactName(self, ContactName):
        field = self.driver.find_element(By.XPATH, self.ContactName_field)
        field.clear()
        field.send_keys(ContactName)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('insert value to "message" input')
    def enter_Message(self, Message):
        field = self.driver.find_element(By.XPATH, self.Message_field)
        field.clear()
        field.send_keys(Message)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('clicking on message button')
    def Message_send_button(self):
        self.driver.find_element(By.XPATH, self.SendMessage_button).click()
        self.driver.implicitly_wait(5)

    def enter_contact_values(self, emals, name, message):
        self.enter_ContactEmail(emals)
        self.enter_ContactName(name)
        self.enter_Message(message)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('clicking on close button')
    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.Close_button).click()
        self.driver.implicitly_wait(5)
        Alt = self.driver.switch_to.alert.text
        print("your selected", Alt, "Thanks!!")
        assert Alt == "Thanks for the message!!"
        self.driver.switch_to.accept()

    def Alert_accepter(self):
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(5)



