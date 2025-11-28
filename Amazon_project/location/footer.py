import time

from selenium.webdriver.common.by import By


class Footer:
    def __init__(self,driver):
        self.driver = driver
        self.india=(By.XPATH,"//a[@id='icp-touch-link-country']")

    def select_location(self):
        for i in range(0, 5000, 300):
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.3)
        time.sleep(5)
        self.driver.find_element(*self.india).click()
        time.sleep(3)





