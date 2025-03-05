import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa_tests.utils import attach
from dotenv import load_dotenv

SELENOID_LOGIN = os.getenv("SELENOID_LOGIN")
SELENOID_PASSWORD = os.getenv("SELENOID_PASS")
SELENOID_URL = os.getenv("SELENOID_URL")


@pytest.fixture(scope="session")
def setup_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_manager(setup_env):
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{SELENOID_LOGIN}:{SELENOID_PASSWORD}@{SELENOID_URL}/wd/hub",
        options=options
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
