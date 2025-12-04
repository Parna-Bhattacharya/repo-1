
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoToWebsite:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown = (By.XPATH, "//span[@class='a-dropdown-prompt']")
        self.option = (By.XPATH, "//ul[@class='a-nostyle a-list-link']//a")
        self.click_goto = (By.XPATH, "//span[@id='icp-save-button']")
        self.wait = WebDriverWait(driver, 10)

    def go_to_website(self):
        logging.info("Clicking dropdown...")
        self.wait.until(EC.element_to_be_clickable(self.dropdown)).click()

    def choose_location(self):
        logging.info("Waiting for country options...")
        options = self.wait.until(EC.presence_of_all_elements_located(self.option))

        for i in options:
            logging.info(f"Found option: {i.text.strip()}")
            if i.text.strip() == "United States":
                logging.info("Clicking on 'United States'")
                self.driver.execute_script("arguments[0].click();", i)
                break

        logging.info("Saving selected country...")
        self.wait.until(EC.element_to_be_clickable(self.click_goto)).click()
