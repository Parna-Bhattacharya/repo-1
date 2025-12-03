import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class HardBook:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.hardcover = (By.XPATH,
            "//a[@aria-label='Apply the filter Hindi to narrow results']//i[@class='a-icon a-icon-checkbox']"
        )

    def get_hardbook(self):
        logging.info("Waiting for Hardcover checkbox to be clickable...")
        hard = self.wait.until(EC.element_to_be_clickable(self.hardcover))

        logging.info("Clicking the Hardcover checkbox.")
        hard.click()
        logging.info("Hardcover checkbox clicked successfully.")
