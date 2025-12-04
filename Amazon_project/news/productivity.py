import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.webdriver.support.wait import WebDriverWait


class Product:
    def __init__(self,driver):
        self.driver = driver
        # self.productivity = (By.XPATH,"//div[@class='padding-left-xsmall padding-right-xsmall flex-container flex-align-items-stretch flex-align-content-flex-start flex-full-width alexa2018 ember background-color-transparent border-color-transparent']//img[@alt='Productivity']")
        self.alexa = (By.XPATH, "//img[@alt='Amazon Alexa Logo']")
        self.smart=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]")
        self.device=(By.XPATH,"//div/ol[@class='a-carousel']/li")
        self.wait=WebDriverWait(self.driver,10)

    def click_alexa(self):
        self.wait.until(EC.element_to_be_clickable(self.alexa)).click()
        logging.info("click Alexa")
        for i in range(0, 600, 50):
            self.driver.execute_script("window.scrollBy(0, 50);")
            time.sleep(0.3)

        self.wait.until(EC.element_to_be_clickable(self.smart)).click()
        logging.info("click smart")
        for i in range(0, 1000, 50):
            self.driver.execute_script("window.scrollBy(0, 50);")
            time.sleep(0.3)
    def click_device(self):
        devices=self.driver.find_elements(*self.device)
        logging.info("click devices")
        count=0
        for i in devices:
            if count==1:
                i.click()
                break
            count+=1



