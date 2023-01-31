import pytest
import allure

from Web.Pages.cart_page import CartPage
from Web.base.test_base import TestBases


class TestCartPage(TestBases):
    @allure.description(" test cart with correct information")
    @pytest.mark.sanity
    def test_cart_page_validly(self):
        self.driver = super().init()
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

    @allure.description("Empty user name test")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_name(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("")
        cart.fill_country_to_purchase("Ethiopia")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()

    @allure.description("empty country")
    @pytest.mark.sanity
    def test_cart_page_with_empty_user_country(self):
        self.driver = super().init()
        cart = CartPage(self.driver)
        cart.cart_page()
        cart.place_order()
        cart.fill_name_to_purchase("Zemene Abinet")
        cart.fill_country_to_purchase("")
        cart.fill_city_to_purchase("Gondar")
        cart.fill_credit_card_to_purchase("65656514502")
        cart.fill_month_to_purchase("March")
        cart.fill_year_to_purchase("2023")
        cart.click_to_purchase()
        cart.click_ok_buttons()

