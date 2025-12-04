import time

from selenium.webdriver.common.by import By


class Cake:
    def __init__(self, driver):
        self.driver = driver
        self.ranges=(By.XPATH,"//ul[@id='filter-p_36']//li")
        # self.brand=(By.XPATH,"//span[@class='a-size-base a-color-base'][normalize-space()='Mother Dairy']")
        # self.mother_diary=(By.XPATH,"//img[@alt='Mother Dairy Ice Cream Cake Black Forest, 1L']")




    def hochpoch(self):
        range=self.driver.find_elements(*self.ranges)
        range[2].click()
        # for i in range:
        #     if i.text=="over ₹400":
        #         i.click()

        # self.driver.find_element(*self.brand).click()
        # time.sleep(3)
        # self.driver.find_element(*self.mother_diary).click()
        # time.sleep(5)
