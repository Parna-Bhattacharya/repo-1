import time

from selenium.webdriver.common.by import By


class BlackFriday:
    def __init__(self, driver):
        self.driver = driver


    def change_address(self):
        for i in range(0, 5000, 300):
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.3)
        time.sleep(5)
