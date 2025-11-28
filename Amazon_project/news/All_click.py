


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AllClick:
    def __init__(self, driver):
        self.driver = driver
        self.all = (By.XPATH, "//a[@id='nav-hamburger-menu']")



    def news(self):
        self.driver.find_element(*self.all).click()

        # Wait for Fire TV anchor tag to actually be clickable
        fire_tv = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Echo & Alexa']"))
        )

        # Scroll into view (important for Amazon)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", fire_tv)
        time.sleep(1)

        fire_tv.click()
        time.sleep(5)

    # def echo(self):
    #     alexa=self.driver.find_elements(By.XPATH,"//section[@aria-labelledby='Content & Resources']//ul/li")
    #     for i in alexa:
    #         if i.text == "Alexa Skills":
    #             i.click()

    def echo(self):
        target = self.driver.find_element(By.XPATH, "//section[@aria-labelledby='Content & Resources']//ul/li/a[normalize-space()='Alexa Skills']")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
        time.sleep(1)

        self.driver.execute_script("arguments[0].click();", target)







