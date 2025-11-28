import time

from selenium.webdriver.common.by import By


class WomanPage:
    def __init__(self, driver):
        self.driver = driver
        self.woman = (By.XPATH, "//span[normalize-space()='Women']")

    def woman_home(self):
        self.driver.find_element(*self.woman).click()
        time.sleep(2)

