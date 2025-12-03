# import time
#
# from selenium.webdriver.common.by import By
#
#
# class AllPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.all = (By.XPATH, "//a[@id='nav-hamburger-menu']")
#         self.see_all=(By.XPATH, "//a[@aria-label='See All Categories']//div[contains(text(),'See all')]")
#         self.book=(By.XPATH, "//ul[@class='hmenu-compress-section']//li[6]//a[1]")
#         # self.indian_book=(By.XPATH,"//a[normalize-space()='Indian Language Books']")
#         self.search_book=(By.XPATH,"//input[@id='twotabsearchtextbox']")
#
#     def all_clicking(self):
#         self.driver.find_element(*self.all).click()
#         time.sleep(2)
#
#     def see_all_clicking(self):
#         self.driver.find_element(*self.see_all).click()
#         time.sleep(4)
#     def book_clicking(self):
#         self.driver.find_element(*self.book).click()
#
#
#
#     def indian_book_clicking(self):
#         book_list_container = self.driver.find_element(By.CSS_SELECTOR, "section[aria-labelledby='Books']")
#
#         if book_list_container:
#             book_list = book_list_container.find_elements(By.CSS_SELECTOR, "ul li a")
#             print(f"book list length {len(book_list)}")
#             assert len(book_list) > 0, "list is empty"
#
#             found = False
#
#             for book in book_list:
#                 print(f"list text are : {book.text}")
#
#                 if book.text.strip() == "Indian Language Books":
#                     # SCROLL to element
#                     self.driver.execute_script("arguments[0].scrollIntoView(true);", book)
#                     time.sleep(1)
#
#                     # CLICK using JavaScript (solves interception)
#                     self.driver.execute_script("arguments[0].click();", book)
#
#                     found = True
#                     break
#
#             if not found:
#                 raise AssertionError("Indian Language Books not found")
#
#         else:
#             raise AssertionError("something wrong: no container found")
#
#     def search_indian_book(self, book_name):
#         box = self.driver.find_element(*self.search_book)
#         # box.clear()
#         box.send_keys(book_name + "\n")
#         time.sleep(5)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class AllPage:
    def __init__(self, driver):
        self.driver = driver
        self.all = (By.XPATH, "//a[@id='nav-hamburger-menu']")
        self.see_all=(By.XPATH, "//a[@aria-label='See All Categories']//div[contains(text(),'See all')]")
        self.book=(By.XPATH, "//ul[@class='hmenu-compress-section']//li[6]//a[1]")
        # self.indian_book=(By.XPATH,"//a[normalize-space()='Indian Language Books']")
        self.search_book=(By.XPATH,"//input[@id='twotabsearchtextbox']")
        self.wait = WebDriverWait(driver, 10)
#

    def all_clicking(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.all)
        )
        element.click()
        logging.info("Clicked on 'All' menu")

    def see_all_clicking(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.see_all)
        )
        element.click()
        logging.info("Clicked on 'See All Categories'")

    def book_clicking(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.book)
        )
        element.click()
        logging.info("Clicked on 'Books' category")

    def indian_book_clicking(self):
        book_list_container = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section[aria-labelledby='Books']"))
        )

        book_list = book_list_container.find_elements(By.CSS_SELECTOR, "ul li a")
        assert len(book_list) > 0, "Book list is empty"

        found = False

        for book in book_list:
            if book.text.strip() == "Indian Language Books":
                self.driver.execute_script("arguments[0].scrollIntoView(true);", book)
                self.wait.until(EC.element_to_be_clickable(book))
                self.driver.execute_script("arguments[0].click();", book)
                found = True
                logging.info("Clicked on 'Indian Language Books'")
                break

        if not found:
            logging.error("Indian Language Books not found")
            raise AssertionError("Indian Language Books not found")

    def search_indian_book(self, book_name):
        box = self.wait.until(
            EC.visibility_of_element_located(self.search_book)
        )
        box.send_keys(book_name + "\n")
        logging.info(f"Searched for Indian book: {book_name}")
