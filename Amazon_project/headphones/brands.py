
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging


class Brand:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.headphone = (By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.brands_names = (By.CSS_SELECTOR, "div#brandsRefinements ul span li span.a-list-item")
        self.noise = (By.CSS_SELECTOR, "div.puis-card-container")
        self.off = (By.CSS_SELECTOR, "div.a-row.a-size-base.a-color-base")

    def search(self, name_headphone):
        logging.info("Searching for headphone: %s", name_headphone)

        # type and hit enter
        search_box = self.wait.until(EC.presence_of_element_located(self.headphone))
        search_box.send_keys(name_headphone + "\n")

        # wait for brand list to load
        brands = self.wait.until(EC.presence_of_all_elements_located(self.brands_names))

        # click Noise brand
        for b in brands:
            if b.text.strip() == "Noise":
                self.wait.until(EC.element_to_be_clickable(b)).click()
                logging.info("Clicked Noise brand")
                break

    def adding(self):
        logging.info("Finding products with 69% off")

        products = self.wait.until(EC.presence_of_all_elements_located(self.noise))
        discounts = self.wait.until(EC.presence_of_all_elements_located(self.off))

        count = 0

        for i in range(len(products)):
            if "69% off" in discounts[i].text:
                count += 1
                add_btn = products[i].find_element(By.XPATH, ".//button[@name='submit.addToCart']")
                self.wait.until(EC.element_to_be_clickable(add_btn)).click()
                logging.info("Added product with 69% off to cart")

        logging.info(f"Total 69% off products = {count}")

        return count
