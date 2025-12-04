# import time
#
# from selenium.webdriver.common.by import By
#
#
# class Footer:
#     def __init__(self,driver):
#         self.driver = driver
#         self.india=(By.XPATH,"//a[@id='icp-touch-link-country']")
#
#     def select_location(self):
#         for i in range(0, 5000, 300):
#             self.driver.execute_script("window.scrollBy(0, 300);")
#             time.sleep(0.3)
#         time.sleep(5)
#         self.driver.find_element(*self.india).click()
#         time.sleep(3)
#
#
#
#
#
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Footer:
    def __init__(self, driver):
        self.driver = driver
        self.india = (By.XPATH, "//a[@id='icp-touch-link-country']")
        self.wait = WebDriverWait(driver, 10)

    def select_location(self):
        logging.info("Scrolling to footer...")
        # Smooth scrolling until 5000 px
        for i in range(0, 5000, 300):
            self.driver.execute_script("window.scrollBy(0, 300);")

        logging.info("Waiting to click country option...")
        self.wait.until(EC.element_to_be_clickable(self.india)).click()
        logging.info("Clicked on country change option.")
