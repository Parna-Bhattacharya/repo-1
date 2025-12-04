import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Popovers:
    def __init__(self,driver):
        self.driver=driver
        self.pop = (By.XPATH, "//span[@id='a-autoid-0-announce']")
        self.popover = (By.XPATH, "//div[@class='a-popover-inner']/ul/li")
        self.adding=(By.XPATH, "//input[@id='add-to-cart-button']")
        self.thanks=(By.XPATH, "//span[@class='a-button a-button-base abb-intl-decline']//input[@type='submit']")
        self.wait=WebDriverWait(self.driver,20)

    def click_popover(self):
        self.wait.until(EC.element_to_be_clickable(self.pop)).click()
        pops=self.driver.find_elements(*self.popover)
        count=0
        for i in pops:
            if count==1:
                i.click()
                break
            count=count+1
            time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.adding)).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.thanks)).click()


