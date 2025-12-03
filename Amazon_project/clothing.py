# import time
#
# from selenium.webdriver.common.by import By
#
#
# class ClothingPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.clothing = (By.XPATH, "//span[@dir='auto'][normalize-space()='Clothing']")
#
#     def clothing_home(self):
#         self.driver.find_element(*self.clothing).click()
#         time.sleep(2)
#
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClothingPage:
    def __init__(self, driver):
        self.driver = driver
        self.clothing = (By.XPATH, "//span[@dir='auto'][normalize-space()='Clothing']")

    def clothing_home(self):
        logging.info("Waiting for 'Clothing' button to become clickable")

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.clothing))

        logging.info("'Clothing' button is clickable, clicking now")
        element.click()

        logging.info("Successfully clicked on 'Clothing' section")
