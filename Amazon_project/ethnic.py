import time

from selenium.webdriver.common.by import By


class EthnicPage:
    def __init__(self, driver):
        self.driver = driver
        self.ethnic = (By.XPATH,"(//span[contains(text(),'Ethnic Wear')])[1]" )
        self.celeb_closet=(By.XPATH,"//li[@id='sobe_d_b_ms_17_2']//img[@alt='2']")
        self.add_to=(By.XPATH,"//button[@id='a-autoid-1-announce']")
        self.add_to_cart=(By.XPATH,"//a[normalize-space()='Go to Cart']")

    def ethnic_home(self):
        self.driver.find_element(*self.ethnic).click()
        time.sleep(2)
        celeb = self.driver.find_element(*self.celeb_closet)

        position = celeb.location['y']


        for i in range(0, position, 300):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(1)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", celeb)
        time.sleep(2)
        celeb.click()
        time.sleep(2)
        # self.driver.find_element(*self.celeb_closet).click()
    def add(self):
        self.driver.find_element(*self.add_to).click()
        time.sleep(2)
    def adds_(self):
        self.driver.find_element(*self.add_to_cart).click()
        time.sleep(4)





