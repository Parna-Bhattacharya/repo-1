import time

from selenium.webdriver.common.by import By


class GoToCart:
    def __init__(self,driver):
        self.driver=driver
        self.go=(By.XPATH,"//a[@href='/cart?ref_=sw_gtc']")
        self.electronic=(By.XPATH,"//a[normalize-space()='Electronics']")
        self.carausal=(By.XPATH,"//div[@class='dcl-container d-page-type-browse d-showcase d-widget-group-9d30a0ed-e36a-4d53-90de-21ac239b287d']//div[@class='a-carousel-col a-carousel-right']//a[@role='button']")
        self.watch=(By.CSS_SELECTOR,"#anonCarousel2 ol.a-carousel li")

    def go_to(self):
        self.driver.find_element(*self.go).click()
        time.sleep(3)

    def electronics(self):
        self.driver.find_element(*self.electronic).click()
        for i in range(0,1500,50):
            self.driver.execute_script("window.scrollBy(0,50);")
            time.sleep(0.3)
        self.driver.find_element(*self.carausal).click()
        time.sleep(2)
        self.driver.find_element(*self.carausal).click()
        time.sleep(2)
    def watches(self):
        smartwatch=self.driver.find_elements(*self.watch)
        count=0
        for i in smartwatch:
            if count==10:
                i.click()
                break
            count=count+1







