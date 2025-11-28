import time

from selenium.webdriver.common.by import By


class ClothingPage:
    def __init__(self, driver):
        self.driver = driver
        self.clothing = (By.XPATH, "//span[@dir='auto'][normalize-space()='Clothing']")

    def clothing_home(self):
        self.driver.find_element(*self.clothing).click()
        time.sleep(2)

