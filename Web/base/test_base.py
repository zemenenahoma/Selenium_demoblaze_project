from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestBases:
    services = Service("C:\\chromedriver.exe")
    driver = webdriver.Chrome(service=services)
    driver.implicitly_wait(10)

    def init(self):
        self.driver.get("https://www.demoblaze.com/ ")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        return self.driver

    def teardown(self):

        self.driver.quit()
