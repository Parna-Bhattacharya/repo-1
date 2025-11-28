import time

from selenium.webdriver.common.by import By


class Tv:
    def __init__(self,driver):
        self.driver=driver
        self.version=(By.CSS_SELECTOR,"ul.dimension-values-list li input[type='submit']")
        self.exchanging=(By.XPATH,"//i[@class='a-icon a-accordion-radio a-icon-radio-inactive']")
        self.phones=(By.ID, "chooseButtonCTA")
    def tv_deal(self):
        for i in range(0, 500, 50):
            self.driver.execute_script("window.scrollBy(0, 50);")
            time.sleep(0.3)
        verions=self.driver.find_elements(*self.version)
        verions[2].click()

        time.sleep(3)
    def exchange(self):
        self.driver.execute_script("window.scrollBy(0, -500);")

        self.driver.find_element(*self.exchanging).click()
    def phone(self):
        element = self.driver.find_element(*self.phones)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

        # Now click
        element.click()
        time.sleep(2)




