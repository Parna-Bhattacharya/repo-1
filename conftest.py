import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    print("\nLaunching browser...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    time.sleep(5)
    driver.maximize_window()
    WebDriverWait(driver, 10)
    yield driver
    print("\nClosing browser...")
    driver.quit()