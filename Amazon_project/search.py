import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.search_box = (By.ID, "twotabsearchtextbox")
        self.result_items = (By.XPATH, "//div[contains(@class, 's-result-item') and @data-asin!='']")
        self.title_xpath = ".//h2//span"
        self.price_xpath = ".//span[@class='a-price-whole']"
        self.add = ".//button[@class='a-button-text']"

    def search_product(self, product_name):
        logging.info("Waiting for search box...")
        box = self.wait.until(EC.visibility_of_element_located(self.search_box))

        logging.info(f"Searching for product: {product_name}")
        box.send_keys(product_name + "\n")

    def get_first_product_details(self):
        logging.info("Waiting for product results...")
        products = self.wait.until(EC.presence_of_all_elements_located(self.result_items))

        if len(products) == 0:
            logging.warning("No products found!")
            return "NO TITLE","NO PRICE"

        for i in range(len(products)):
            if i == 1:
                title = products[i].find_element(By.XPATH, self.title_xpath).text
                price = products[i].find_element(By.XPATH, self.price_xpath).text

                logging.info(f"Product title: {title}")
                logging.info(f"Product price: {price}")

                return title, price

    def get_products_above_price(self, min_price):
        logging.info("Waiting for product list to load...")
        products = self.wait.until(EC.presence_of_all_elements_located(self.result_items))

        for product in products:
            price_text = product.find_element(By.XPATH, self.price_xpath).text.replace(",", "").strip()

            if price_text.isdigit():
                price = int(price_text)

                if price >= min_price:
                    logging.info(f"Found product above {min_price}: {price} → Clicking Add button")

                    add_btn = product.find_element(By.XPATH, self.add)
                    self.wait.until(EC.element_to_be_clickable(add_btn))
                    add_btn.click()

                    logging.info("Product added successfully.")
