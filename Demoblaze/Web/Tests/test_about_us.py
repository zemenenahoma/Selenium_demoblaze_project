import time

import allure

from Demoblaze.Web.Base.Base_test import Base_test
from Demoblaze.Web.Page.page_about_us import About_us_page

class Test_about_us(Base_test):

    @allure.description('Navigate to "about us" page correctly')
    def test_click_on_about_us_page(self):
        driver = self.driver
        aboutUS = About_us_page(driver)
        aboutUS.open()
        aboutUS.aboutUs_link()

    @allure.description('Click play  " video will be open ')
    def test_click_video_play(self):
        driver = self.driver
        aboutUS = About_us_page(driver)
        aboutUS.open()
        aboutUS.aboutUs_link()
        aboutUS.vedio_play()
        aboutUS.vedio_puse_button()
        aboutUS.vedio_puse_button()
        aboutUS.vedio_speaker_button()
        aboutUS.vedio_speaker_button()
        aboutUS.vedio_fullScreen_button()
        aboutUS.vedio_fullScreen_button()

        #aboutUS.Viedo_close_button()



