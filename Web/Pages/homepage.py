from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Web.Locators.hompage_locators import CategoryPhoneLocator
from Web.Locators.cart_locators import CartLocators

import time

from Web.Pages.cart_page import CartPage


class HomePage(CategoryPhoneLocator, CartLocators):
    def __init__(self, driver):
        self.driver = driver

    def log_check(self):
        logo = self.driver.find_element(By.XPATH, self.logo_xpath)
        logo.is_displayed()

    def category_phone(self):
        cat = self.driver.find_element(By.XPATH, self.phone_xpath)
        cat.click()

    def samsung_click(self):
        sums = self.driver.find_element(By.XPATH, self.samsung_xpath)
        sums.click()

    def samsung_add_cart(self):
        sums_add_cart = self.driver.find_element(By.XPATH, self.samsung_add_cart_xpath)
        sums_add_cart.click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(10)
        self.driver.back()
        self.driver.back()

    def category_laptop(self):
        cat = self.driver.find_element(By.XPATH, self.laptop_xpath)
        cat.click()

    def del_laptop_click(self):
        del_s = self.driver.find_element(By.XPATH, self.deli7_xpath)
        del_s.click()

    def del_lap_top_add_cart(self):
        sums_add_cart = self.driver.find_element(By.XPATH, self.deli7_add_cart_xpath)
        sums_add_cart.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(3)
        self.driver.back()
        self.driver.back()

    def category_monitor(self):
        moni = self.driver.find_element(By.XPATH, self.monitor_xpath)
        moni.click()

    def apple_monitor(self):
        apple = self.driver.find_element(By.XPATH, self.apple_monitor_xpath)
        apple.click()

    def apple_monitor_add_to_card(self):
        app_mon = self.driver.find_element(By.XPATH, self.apple_monitor_add_cart_xpath)
        app_mon.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alt = self.driver.switch_to.alert.text
        print("your selected ", alt, "Thanks!!!")
        assert alt == "Product added"
        self.driver.switch_to.alert.accept()

    def goto_cart_page_to_fill_forms(self):
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()
