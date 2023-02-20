import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Locators.locators_cart import Cart_locators

class CartPage(Base_test, Cart_locators):

    @allure.description('click CartLink on home ')
    @pytest.mark.sanity
    def CartLink(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Cart_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('click OrederPlace_button in cart')
    @pytest.mark.sanity
    def OrederPlace_button(self):
        self.driver.find_element(By.XPATH, self.Oreder_place_button).click()
        self.driver.implicitly_wait(5)


    @allure.description('Insert name on Name Field')
    @pytest.mark.sanity
    def NameField(self, NameField):
        self.driver.find_element(By.XPATH, self.Name_field).clear()
        self.driver.find_element(By.XPATH, self.Name_field).send_keys(NameField)
        self.driver.implicitly_wait(5)


    @allure.description('Insert Country on Country_Field')
    @pytest.mark.sanity
    def CountryField(self, CountryField):
        self.driver.find_element(By.XPATH, self.Country_field).clear()
        self.driver.find_element(By.XPATH, self.Country_field).send_keys(CountryField)
        self.driver.implicitly_wait(5)


    @allure.description('Insert City on City_Field')
    @pytest.mark.sanity
    def Cityfield(self, Cityfield):
        self.driver.find_element(By.XPATH, self.City_field).clear()
        self.driver.find_element(By.XPATH, self.City_field).send_keys(Cityfield)
        self.driver.implicitly_wait(5)


    @allure.description('Insert Credit-Cart numbers on Credit-card-Field')
    @pytest.mark.sanity
    def CreditFard(self, CreditFard):
        self.driver.find_element(By.XPATH, self.Credit_card).clear()
        self.driver.find_element(By.XPATH, self.Credit_card).send_keys(CreditFard)
        self.driver.implicitly_wait(5)


    @allure.description('Insert Month on Month-Field')
    @pytest.mark.sanity
    def MonthField(self, MonthField):
        self.driver.find_element(By.XPATH, self.Month_field).clear()
        self.driver.find_element(By.XPATH, self.Month_field).send_keys(MonthField)
        self.driver.implicitly_wait(5)


    @allure.description('Insert Year on Year-Field')
    @pytest.mark.sanity
    def Yearfeild(self, Yearfeild):
        self.driver.find_element(By.XPATH, self.Year_feild).clear()
        self.driver.find_element(By.XPATH, self.Year_feild).send_keys(Yearfeild)
        self.driver.implicitly_wait(5)


    @allure.description('click purchase button')
    @pytest.mark.sanity
    def PurchaseButton(self):
        self.driver.find_element(By.XPATH, self.Purchase_button).click()
        self.driver.implicitly_wait(5)


    @allure.description('click Close button')
    @pytest.mark.sanity
    def CloseField(self):
        self.driver.find_element(By.XPATH, self.Close_field).click()
        self.driver.implicitly_wait(5)


    @allure.description('click delete button')
    @pytest.mark.sanity
    def DeletOrder(self):
        self.driver.find_element(By.XPATH, self.Delet_order).click()


    def enter_cart_field_values(self, Name, Country, City, CreditCard, Month, Year):
        self.NameField(Name)
        self.CountryField(Country)
        self.Cityfield(City)
        self.CreditFard(CreditCard)
        self.MonthField(Month)
        self.Yearfeild(Year)
        self.driver.implicitly_wait(5)