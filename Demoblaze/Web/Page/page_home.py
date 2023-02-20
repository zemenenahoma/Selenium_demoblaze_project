import time
import pytest
import allure
from selenium.webdriver.common.by import By
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Locators.locators_home import Home_locators


class HomePage(Base_test, Home_locators):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        super().init()

    @allure.description('Navigate to home page')
    @pytest.mark.sanity
    def homeLink(self):
        self.driver.find_element(By.XPATH, self.Home_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('click Next slide  button')
    @pytest.mark.sanity
    def NextSlide_Click(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Next_slide_mage).click()
        self.driver.implicitly_wait(5)

    @allure.description('click Previous slide  button')
    @pytest.mark.sanity
    def PreviousSlide_click(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Previous_slide_image).click()
        self.driver.implicitly_wait(5)

    @allure.description('click Next button')
    @pytest.mark.sanity
    def NextSlide_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Next_button).click()
        self.driver.implicitly_wait(5)

    @allure.description('click Previous slide  button')
    @pytest.mark.sanity
    def PreviousSlide_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Previous_buttom).click()
        self.driver.implicitly_wait(5)

    @allure.description('Scroll down the page')
    @pytest.mark.sanity
    def scroll_page_down(self):
        self.driver.implicitly_wait(5)
        self. driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_page_up(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(1300, 0);")
        self.driver.implicitly_wait(5)




    @allure.description('click categories button')
    @pytest.mark.sanity
    def CatagoriesButton(self):
        self.driver.find_element(By.XPATH, self.Catagories_button).click()
        self.driver.implicitly_wait(5)

    @allure.description('click phone button')
    @pytest.mark.sanity
    def Phone_categories(self):
        self.driver.find_element(By.XPATH, self.Phone_categories_button).click()
        self.driver.implicitly_wait(5)

    @allure.description('click Samsung_galaxys7')
    @pytest.mark.sanity
    def Samsung_galaxys7(self):
        samseng = self.driver.find_element(By.XPATH, self.Samsung_galaxys7_button)
        samseng.click()
        self.driver.implicitly_wait(5)

    @allure.description('click NokiaLumia1520')
    @pytest.mark.sanity
    def NokiaLumia1520(self):
        Nokia = self.driver.find_element(By.XPATH, self.Nokia_Lumia1520_button)
        Nokia.click()
        self.driver.implicitly_wait(5)

    @allure.description('click Nexus6Phone_link')
    @pytest.mark.sanity
    def Nexus6Phone_link(self):
        self.driver.find_element(By.XPATH, self.Nexus6_phone_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('click laptop_categories')
    @pytest.mark.sanity
    def laptop_categories(self):
        self.driver.find_element(By.XPATH, self.Laptop_caregories_button).click()
        self.driver.implicitly_wait(5)

    @allure.description('click dell_I7_8_gb_laptop')
    @pytest.mark.sanity
    def dell_I7_8_gb_laptop(self):
        self.driver.find_element(By.XPATH, self.Dell_I7_8_gb_laptop_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('click sony_vaio_15_laptop')
    @pytest.mark.sanity
    def sony_vaio_15_laptop(self):
        self.driver.find_element(By.XPATH, self.Sony_vaio_15_laptop_link).click()
        self.driver.implicitly_wait(5)


    @allure.description('click macBook_air_laptop')
    @pytest.mark.sanity
    def Delli7_click_laptop(self):
        self.driver.find_element(By.XPATH, self.Delli7_laptop_link).click()
        self.driver.implicitly_wait(5)


    @allure.description('click moniters_caregories')
    @pytest.mark.sanity
    def moniters_caregories(self):
        self.driver.find_element(By.XPATH, self.Moniters_caregories_button).click()
        self.driver.implicitly_wait(5)

    @allure.description('click apple_monitors_24_monitors')
    @pytest.mark.sanity
    def apple_monitors_24_monitors(self):
        self.driver.find_element(By.XPATH, self.Apple_monitors_24_monitors_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('click aSUS_Full_HD_monitors')
    @pytest.mark.sanity
    def aSUS_Full_HD_monitors(self):
        self.driver.find_element(By.XPATH, self.ASUS_Full_HD_monitors_link).click()
        self.driver.implicitly_wait(5)

    @allure.description('click AddTocart')
    @pytest.mark.sanity
    def AddTocart(self):
        self.driver.find_element(By.XPATH, self.Add_to_cart).click()
        self.driver.implicitly_wait(5)

    @allure.description('click ok ')
    @pytest.mark.sanity
    def SwitchAlert(self):
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(5)

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

