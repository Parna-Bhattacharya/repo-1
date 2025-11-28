import time

from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button=(By.XPATH, "//a[@id='nav-cart']")

        self.product_button=(By.XPATH, "//input[@name='proceedToRetailCheckout']")
    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        time.sleep(3)
    def proceed_to_cart(self):

        self.driver.find_element(*self.product_button).click()
        time.sleep(3)

