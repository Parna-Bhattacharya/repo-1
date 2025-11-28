import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.fashion = (By.XPATH, "//a[normalize-space()='Fashion']")

    def fashion_home(self):
        self.driver.find_element(*self.fashion).click()
        time.sleep(2)

