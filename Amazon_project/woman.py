import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WomanPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.woman = (By.XPATH, "//span[normalize-space()='Women']")

    def woman_home(self):
        logging.info("Waiting for Women button to be clickable...")
        women_btn = self.wait.until(EC.element_to_be_clickable(self.woman))

        logging.info("Women button is clickable. Clicking now.")
        women_btn.click()
