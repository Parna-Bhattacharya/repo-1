import time
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Deal:
    def __init__(self,driver):
        self.driver=driver
        self.nav=(By.CSS_SELECTOR,"div ul li div a.nav-a")

    def today_deal(self):
        # wait until navigation items are present
        nav_click = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.nav)
        )

        clicked = False
        for i in nav_click:
            if i.text.strip() == "Today's Deals":
                i.click()
                clicked = True
                break

        if not clicked:
            print("Today's Deal option not found!")

        time.sleep(3)

