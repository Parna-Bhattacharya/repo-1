from selenium.webdriver.common.by import By
import time


class AmazonPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.result_items = (By.XPATH, "//div[contains(@class, 's-result-item') and @data-asin!='']")
        self.title_xpath = ".//h2//span"
        self.price_xpath = ".//span[@class='a-price-whole']"

        self.add=".//button[@class='a-button-text']"



    def search_product(self, product_name):
        box = self.driver.find_element(*self.search_box)
        # box.clear()
        box.send_keys(product_name + "\n")
        time.sleep(5)

    def get_first_product_details(self):
        products = self.driver.find_elements(*self.result_items)
        # print("Number of products found:", len(products))

        if len(products) == 0:
            print("No products found!")
            return "No title", "No price"
        # all_products = []
        for i in range(len(products)):
            if i==1:
                title = products[i].find_element(By.XPATH, self.title_xpath).text
                price = products[i].find_element(By.XPATH, self.price_xpath).text



                return title, price,#deliv

    def get_products_above_price(self, min_price):
        products = self.driver.find_elements(*self.result_items)
        print("Number of products found:", len(products))



        for product in products:
            price_text = product.find_element(By.XPATH, self.price_xpath).text.replace(",", "").strip()
            if price_text.isdigit():
                price = int(price_text)
                if price >= min_price:

                    product.find_element(By.XPATH, self.add).click()
                    time.sleep(2)


