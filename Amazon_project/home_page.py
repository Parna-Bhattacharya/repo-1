import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.fashion = (By.XPATH, "//a[normalize-space()='Fashion']")

    def fashion_home(self):
        logging.info("Waiting for Fashion button to be clickable...")
        fashion_btn = self.wait.until(EC.element_to_be_clickable(self.fashion))
        logging.info("Fashion button is clickable. Clicking now.")
        fashion_btn.click()
