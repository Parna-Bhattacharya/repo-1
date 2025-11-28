import time

from selenium.webdriver.common.by import By


class Deal:
    def __init__(self,driver):
        self.driver=driver
        self.nav=(By.CSS_SELECTOR,"div ul li div a.nav-a")

    def today_deal(self):
        nav_click=self.driver.find_elements(*self.nav)
        nav_click[5].click()
        time.sleep(5)
