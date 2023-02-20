import time
import pytest
from selenium.webdriver.common.by import By
from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Page.page_home import HomePage
import allure


class Test_home(Base_test):

    @allure.description('Navigate to login page correctly')
    @pytest.mark.sanity
    def test_scroll_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.scroll_page_down()
        login_page.scroll_page_up()

    @allure.description(' next silde and previous slide chenge image ')
    @pytest.mark.sanity
    def test_click_slide_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.NextSlide_Click()
        login_page.PreviousSlide_click()

    @allure.description('Click next button and previous button : change next and previous page ')
    @pytest.mark.sanity
    def test_click_next_button(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.NextSlide_button()

    def test_click_pre_button(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.PreviousSlide_button()

    @allure.description('Navigate to login page correctly')
    @pytest.mark.sanity
    def test_homeLink_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()

    @allure.description('categorues link open next page')
    @pytest.mark.sanity
    def test_Caregoreis_link_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.CatagoriesButton()
        login_page.Phone_categories()

    @allure.description('categories of phone Samsung galaxys7 open next page')
    @pytest.mark.sanity
    def test_Samsung_galaxys7_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.Samsung_galaxys7()
        time.sleep(3)

    @allure.description('categories of phone NokiaLumia1520 open next page')
    @pytest.mark.sanity
    def test_NokiaLumia1520_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.NokiaLumia1520()
        time.sleep(3)

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_Nexus6Phone_link_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.Nexus6Phone_link()
        time.sleep(3)

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_laptop_categories_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.laptop_categories()

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_LaptopsLinks_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.laptop_categories()
        login_page.dell_I7_8_gb_laptop()
        time.sleep(3)
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.laptop_categories()
        login_page.sony_vaio_15_laptop()
        time.sleep(3)



    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_moniters_caregories_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.moniters_caregories()


    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_monitorsLink_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.moniters_caregories()
        login_page.apple_monitors_24_monitors()
        login_page.AddTocart()
        login_page.SwitchAlert()

        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.moniters_caregories()
        login_page.aSUS_Full_HD_monitors()
        login_page.AddTocart()
        login_page.SwitchAlert()
        login_page.CartLink()
        time.sleep(3)
    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_addtocart_click2(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.moniters_caregories()
        login_page.apple_monitors_24_monitors()
        login_page.AddTocart()
        login_page.SwitchAlert()

        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.NokiaLumia1520()
        login_page.AddTocart()
        login_page.SwitchAlert()

        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.moniters_caregories()
        login_page.aSUS_Full_HD_monitors()
        login_page.AddTocart()
        login_page.SwitchAlert()

        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.Phone_categories()
        login_page.Samsung_galaxys7()
        login_page.AddTocart()
        login_page.SwitchAlert()
        login_page.CartLink()
        time.sleep(3)

    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_addtocart_click(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.CatagoriesButton()
        login_page.Phone_categories()
        login_page.Samsung_galaxys7()
        login_page.AddTocart()
        login_page.SwitchAlert()
        login_page.CartLink()
        time.sleep(3)

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
        ok_button = self.driver.title
        assert ok_button == "STORE"


    @allure.description('categories of phone Nexus6Phone open next page')
    @pytest.mark.sanity
    def test_Nokia_lumia1520_E2E_datas(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.CatagoriesButton()
        login_page.Phone_categories()
        login_page.NokiaLumia1520()
        login_page.AddTocart()
        login_page.SwitchAlert()
        time.sleep(3)
        login_page.CartLink()
        login_page.OrederPlace_button()
        login_page.enter_cart_field_values('Alex', 'Israel', 'Tel Aviv', '1234567', 'June', '2023')
        login_page.PurchaseButton()
        ok_button = self.driver.title
        assert ok_button == "STORE"

    @allure.description('categories of phone Nexus6Phone open next page')
    def test_Nexus6_E2E_Phone_datas(self):
        driver = self.driver
        login_page = HomePage(driver)
        login_page.open()
        login_page.homeLink()
        login_page.CatagoriesButton()
        login_page.Phone_categories()
        login_page.Nexus6Phone_link()
        login_page.AddTocart()
        login_page.SwitchAlert()
        login_page.CartLink()
        login_page.OrederPlace_button()
        login_page.enter_cart_field_values('Alex', 'Israel', 'Tel Aviv', '1234567', 'June', '2023')
        login_page.PurchaseButton()
        ok_button = self.driver.title
        assert ok_button == "STORE"

