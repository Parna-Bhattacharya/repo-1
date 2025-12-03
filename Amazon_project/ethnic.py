import time
import logging

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EthnicPage:
    def __init__(self, driver):
        self.driver = driver
        self.ethnic = (By.XPATH, "(//span[contains(text(),'Ethnic Wear')])[1]")
        self.celeb_closet = (By.XPATH, "//li[@id='sobe_d_b_ms_17_2']//img[@alt='2']")
        self.add_to = (By.XPATH, "//button[@id='a-autoid-1-announce']")
        self.add_to_cart = (By.XPATH, "//a[normalize-space()='Go to Cart']")
        self.wait = WebDriverWait(driver, 10)

    def ethnic_home(self):
        logging.info("Clicking on Ethnic Wear")
        element = self.wait.until(EC.element_to_be_clickable(self.ethnic))
        element.click()

        logging.info("Finding celebrity closet image")
        celeb = self.wait.until(EC.presence_of_element_located(self.celeb_closet))

        position = celeb.location['y']
        logging.info(f"Scrolling till y position: {position}")

        for i in range(0, position, 300):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(1)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", celeb)
        time.sleep(2)
        celeb.click()
        logging.info("Clicked on Celebrity Closet item")

    def add(self):
        logging.info("Clicking on Add To button")
        add_btn = self.wait.until(EC.element_to_be_clickable(self.add_to))
        add_btn.click()
        logging.info("Add To button clicked")

    # def adds_(self):
    #     logging.info("Clicking on Go to Cart")
    #     cart = self.wait.until(EC.element_to_be_clickable(self.add_to_cart))
    #     cart.click()
    #     logging.info("Go to Cart clicked")
    from selenium.common.exceptions import StaleElementReferenceException

    def adds_(self):
        logging.info("Waiting for 'Go to Cart' button to appear and be clickable")

        for _ in range(3):  # try 3 times
            try:
                cart = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.add_to_cart)
                )
                cart.click()
                logging.info("'Go to Cart' clicked successfully")
                return
            except StaleElementReferenceException:
                logging.warning("Stale element, retrying Go to Cart click...")



