from selenium.webdriver.common.by import By


class HardBook:
    def __init__(self, driver):
        self.driver = driver

        self.hardcover = (By.XPATH, "//a[@aria-label='Apply the filter Hindi to narrow results']//i[@class='a-icon a-icon-checkbox']")

    def get_hardbook(self):

        self.driver.find_element(*self.hardcover).click()

