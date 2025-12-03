import logging
import pytest
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        filename="my_test.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filemode="a",
    )
    logging.info("========== Test Session Started ==========")


@pytest.fixture
def driver():
    logging.info("Launching browser...")
    print("\nLaunching browser...")

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    yield driver

    logging.info("Closing browser...")
    print("\nClosing browser...")
    driver.quit()
