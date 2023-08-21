import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common import options

# load .env
load_dotenv()

selenium_hub_url = os.getenv("SELENIUM_HUB_URL")


def main():
    try:
        # Default
        driver = None

        # Initialize
        driver = init_webdriver()

        # Access to GitHub
        driver.get('https://github.com')

    except Exception as e:
        print(e)
    finally:
        if driver:
            # Quit
            driver.quit()


def init_webdriver() -> webdriver.Chrome:
    """Initialize ChromeWebDriver

    Returns:
        webdriver.Chrome: ChromeWebDriver
    """
    # Create
    driver = webdriver.Remote(command_executor=selenium_hub_url)

    # Maximize
    driver.maximize_window()

    return driver


if __name__ == "__main__":
    main()
