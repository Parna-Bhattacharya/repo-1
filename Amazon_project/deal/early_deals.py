import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EarlyDeal:
    def __init__(self,driver):
        self.driver=driver
        self.carousal_button=(By.XPATH,"//a[@class='a-carousel-goto-nextpage']")
        self.element = (By.CSS_SELECTOR, "li.a-carousel-card.dcl-carousel-element")
        self.wait=WebDriverWait(driver,10)
    def early_deal(self):
        self.driver.find_element(*self.carousal_button).click()
        time.sleep(2)
        self.driver.find_element(*self.carousal_button).click()
        time.sleep(2)
    def click_element(self):
        elements=self.driver.find_elements(*self.element)
        elements[12].click()
        time.sleep(2)