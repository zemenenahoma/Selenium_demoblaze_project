import time

from selenium.webdriver.common.by import By
from Web.Locators.cart_locators import CartLocators


class CartPage(CartLocators):
    def __init__(self, driver):
        self.driver = driver

    def cart_page(self):
        cart = self.driver.find_element(By.ID, self.cart_element_id)
        cart.click()

    def place_order(self):
        place_orders = self.driver.find_element(By.XPATH, self.place_order_xpath)
        place_orders.click()

    def fill_name_to_purchase(self, name):
        names = self.driver.find_element(By.ID, self.name_id)
        names.send_keys(name)

    def fill_country_to_purchase(self, country):
        countries = self.driver.find_element(By.ID, self.country_id)
        countries.send_keys(country)

    def fill_city_to_purchase(self, citys):
        city = self.driver.find_element(By.ID, self.city_id)
        city.send_keys(citys)

    def fill_credit_card_to_purchase(self, card):
        cards = self.driver.find_element(By.ID, self.credit_card_id)
        cards.send_keys(card)

    def fill_month_to_purchase(self, mon):
        month = self.driver.find_element(By.ID, self.month_id)
        month.send_keys(mon)

    def fill_year_to_purchase(self, yer):
        years = self.driver.find_element(By.ID, self.year_id)
        years.send_keys(yer)

    def click_to_purchase(self):
        purchase = self.driver.find_element(By.XPATH, self.purchase_xpath)
        purchase.click()
        self.driver.implicitly_wait(10)

        alt = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]").text
        assert alt == "Thank you for your purchase!"
        print(alt)

    def click_ok_buttons(self):
        ok = self.driver.find_element(By.XPATH, self.ok_button)
        ok.click()

