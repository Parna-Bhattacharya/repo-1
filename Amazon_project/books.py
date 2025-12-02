# from selenium.webdriver.common.by import By
#
#
# class Book:
#     def __init__(self, driver):
#         self.driver = driver
#         self.tommorow=(By.XPATH,"//span[contains(text(),'Get It by Tomorrow')]")
#         self.paperbook=(By.XPATH,"//span[@class='a-size-base a-color-base'][normalize-space()='Hardcover']")
#         self.hardcover=(By.XPATH,"//span[contains(text(),'Paperback')]")
#         self.format=(By.XPATH,"//ul[@id='filter-p_n_binding_browse-bin']")
#
#
#     def get_it_tommorow(self):
#         self.driver.find_element(*self.tommorow).click()
#         for i in self.format:
#             if  i.strip() == "Paperback":
#                 self.driver.find_element(*self.hardcover).click()
#             else:
#                 self.driver.find_element(*self.paperbook).click()
#
from selenium.webdriver.common.by import By

class Book:
    def __init__(self, driver):
        self.driver = driver
        self.tommorow = (By.XPATH, "//span[contains(text(),'Get It by Tomorrow')]")
        self.paperback = (By.XPATH,"//span[contains(text(),'Paperback')]")
        self.hardcover = (By.XPATH,"//span[@class='a-size-base a-color-base'][normalize-space()='Hardcover']")
        # self.add_buttoon=(By.XPATH,"//button[@id='a-autoid-62-announce']")

    def get_it_tommorow(self):
        self.driver.find_element(*self.tommorow).click()

        # list of both options
        options = [self.paperback, self.hardcover]

        # loop through both
        for opt in options:
            elements = self.driver.find_elements(*opt)
            if elements:
                elements[0].click()
                break
        # self.driver.find_element(*self.add_buttoon).click()