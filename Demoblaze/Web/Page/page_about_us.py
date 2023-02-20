import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Locators.locators_aboutUs import aboutUS_locators


class About_us_page(Base_test, aboutUS_locators):

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    @allure.description('Navigate to about-Us page')
    def open(self, ):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL_demo)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver


    @allure.step
    @allure.description('clicking on about-us button - should navigate to "about us" page')
    def aboutUs_link(self):
        self.driver.find_element(By.XPATH, self.About_Us_Page_link).click()
        self.driver.implicitly_wait(5)

    def vedio_play(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Viedo_play_button).click()
        self.driver.implicitly_wait(20)

    @allure.step
    @allure.description('clicking on pause video button - should  to pause')
    def vedio_puse_button(self):
        self.driver.find_element(By.XPATH, self.Viedo_pause_button).click()
        self.driver.implicitly_wait(5)
    @allure.step
    @allure.description('clicking on speaker button - should mute sound ')
    def vedio_speaker_button(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Viedo_speaker_button).click()
        self.driver.implicitly_wait(5)
    @allure.step
    @allure.description('clicking on full screen button - should full screen of video')
    def vedio_fullScreen_button(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Viedo_fullScreen_button).click()
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('clicking on close button - should close video')
    def vedio_fullScreen_button(self):
        self.driver.find_element(By.XPATH, self.Viedo_close_button).click()
        self.driver.implicitly_wait(5)