import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Cakes:
    def __init__(self, driver):
        self.driver = driver

        self.delivery=(By.XPATH, "(//input[@aria-labelledby='freshAddToCartButton-announce'])[1]")

    def hochpochss(self):
        self.driver.find_element(*self.delivery).click()
        time.sleep(5)