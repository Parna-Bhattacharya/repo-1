import logging
import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file = os.path.join("logs", "my_test.log")
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename=log_file,
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
