import time

from selenium.webdriver.common.by import By


class Popovers:
    def __init__(self,driver):
        self.driver=driver
        self.pop = (By.XPATH, "//span[@id='a-autoid-0-announce']")
        self.popover = (By.XPATH, "//div[@class='a-popover-inner']/ul/li")
        self.adding=(By.XPATH, "//input[@id='add-to-cart-button']")
        self.thanks=(By.XPATH, "//span[@class='a-button a-button-base abb-intl-decline']//input[@type='submit']")

    def click_popover(self):
        self.driver.find_element(*self.pop).click()
        pops=self.driver.find_elements(*self.popover)
        count=0
        for i in pops:
            if count==1:
                i.click()
                break
            count=count+1
            time.sleep(3)

        self.driver.find_element(*self.adding).click()
        time.sleep(3)
        self.driver.find_element(*self.thanks).click()
        time.sleep(3)



