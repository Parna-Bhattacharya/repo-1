import time

from selenium.webdriver.common.by import By


class FreshVegetable:
    def __init__(self, driver):
        self.driver = driver
        self.fresh=(By.XPATH,"//button[@aria-label='Fresh Details']")
        self.fresh_=(By.XPATH,"//img[@alt='Amazon Fresh']")
        self.cake=(By.XPATH,"//input[@id='twotabsearchtextbox']")

    def click_fresh(self):
        self.driver.find_element(*self.fresh).click()
        self.driver.find_element(*self.fresh_).click()

    def search_icecream(self, cake_name):
        box = self.driver.find_element(*self.cake)
        # box.clear()
        box.send_keys(cake_name + "\n")
        time.sleep(5)
