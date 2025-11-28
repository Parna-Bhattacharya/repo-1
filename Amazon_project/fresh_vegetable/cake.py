import time

from selenium.webdriver.common.by import By


class Cake:
    def __init__(self, driver):
        self.driver = driver
        self.range=(By.XPATH,"//span[contains(text(),'Over ₹450')]")
        self.brand=(By.XPATH,"//span[@class='a-size-base a-color-base'][normalize-space()='Mother Dairy']")
        self.mother_diary=(By.XPATH,"//img[@alt='Mother Dairy Ice Cream Cake Black Forest, 1L']")



    def hochpoch(self):
        self.driver.find_element(*self.range).click()
        self.driver.find_element(*self.brand).click()
        time.sleep(3)
        self.driver.find_element(*self.mother_diary).click()
        time.sleep(5)
