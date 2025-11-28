# import time
#
# from selenium.webdriver.common.by import By
#
#
# class GoToWebsite:
#     def __init__(self, driver):
#         self.driver = driver
#         self.dropdown=(By.XPATH,"//span[@class='a-dropdown-prompt']")
#         self.option = (By.CSS_SELECTOR,"div ul li a.a-dropdown-link")
#
#     def go_to_website(self):
#         self.driver.find_element(*self.dropdown).click()
#         time.sleep(3)
#     def choose_location(self):
#         options=self.driver.find_elements(*self.option)
#         for i in options:
#             if i.text=="United States":
#                 i.click()
#         time.sleep(3)


#
#
#
# import time
# from selenium.webdriver.common.by import By
#
# class GoToWebsite:
#     def __init__(self, driver):
#         self.driver = driver
#         self.dropdown = (By.XPATH, "//span[@class='a-dropdown-prompt']")
#         self.option = (By.XPATH, "//ul[@class='a-nostyle a-list-link']//a")
#         self.click_goto=(By.XPATH, "//input[@class='a-button-input']")
#
#     def go_to_website(self):
#         self.driver.find_element(*self.dropdown).click()
#         time.sleep(3)
#
#     def choose_location(self):
#         options = self.driver.find_elements(*self.option)
#         for i in options:
#             if i.text.strip() == "United States":
#                 i.click()
#             print("showing usa")
#             time.sleep(3)
#
#
#         self.driver.find_element(*self.click_goto).click()
#         time.sleep(9)


import time
from selenium.webdriver.common.by import By

class GoToWebsite:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown = (By.XPATH, "//span[@class='a-dropdown-prompt']")
        self.option = (By.XPATH, "//ul[@class='a-nostyle a-list-link']//a")
        self.click_goto = (By.XPATH, "//span[@id='icp-save-button']")

    def go_to_website(self):
        self.driver.find_element(*self.dropdown).click()
        time.sleep(2)

    def choose_location(self):
        options = self.driver.find_elements(*self.option)

        for i in options:
            print("Found:", i.text.strip())
            if i.text.strip() == "United States":
                self.driver.execute_script("arguments[0].click();", i)
                print("Clicked USA")
                break

        time.sleep(2)
        self.driver.find_element(*self.click_goto).click()
        time.sleep(5)


