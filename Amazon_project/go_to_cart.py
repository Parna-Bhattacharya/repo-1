import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cart_button = (By.XPATH, "// a[ @ id = 'nav-cart']")
        # // a[ @ id = 'nav-cart']
        self.product_button = (By.XPATH, "//input[@name='proceedToRetailCheckout']")

    def go_to_cart(self):
        logging.info("Waiting for Cart button to be clickable...")
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        logging.info("Cart button is clickable. Clicking now.")
        cart.click()

    def proceed_to_cart(self):
        logging.info("Waiting for Proceed to Checkout button to be clickable...")
        proceed = self.wait.until(EC.element_to_be_clickable(self.product_button))
        logging.info("Proceed to Checkout button is clickable. Clicking now.")
        proceed.click()
