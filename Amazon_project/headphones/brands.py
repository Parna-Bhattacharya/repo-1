from selenium.webdriver.common.by import By

import time


class  Brand:
    def __init__(self,driver):
        self.driver=driver
        self.headphone=(By.XPATH,"//input[@id='twotabsearchtextbox']")
        self.brands_names=(By.CSS_SELECTOR,"div#brandsRefinements ul span li span.a-list-item")
        self.noise=(By.CSS_SELECTOR,"div.puis-card-container")
        self.off=(By.CSS_SELECTOR,"div.a-row.a-size-base.a-color-base")
        # self.add_cart=(By.XPATH,"//button[@class='a-button-text' and text()='Add to cart']")



    def search(self,name_headphone):
        brands = self.driver.find_element(*self.headphone)
        # box.clear()
        brands.send_keys( name_headphone+ "\n")
        time.sleep(5)
        b=self.driver.find_elements(*self.brands_names)
        for i in b:
            if i.text=="Noise":
                i.click()
                break
        time.sleep(5)
        for i in range(0, 600, 50):
            self.driver.execute_script("window.scrollBy(0, 50);")
            time.sleep(0.3)

    def adding(self):
        products = self.driver.find_elements(*self.noise)
        discounts = self.driver.find_elements(*self.off)

        count = 0

        for i in range(len(products)):
            if "69% off" in discounts[i].text:
                count += 1
                products[i].find_element(By.XPATH, ".//button[@name='submit.addToCart']").click()
                time.sleep(3)



        print("Total 69% off products =", count)
        return count




