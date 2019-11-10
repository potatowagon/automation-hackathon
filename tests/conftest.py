import os
import platform

import pytest
from selenium import webdriver

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
opened_browsers = []

@pytest.fixture()
def hackathon_app_v1():
    return "https://demo.applitools.com/hackathon.html"

@pytest.fixture()
def hackathon_app_v2():
    return "https://demo.applitools.com/hackathonV2.html"

@pytest.fixture()
def chrome_driver():
    if is_windows():
        return os.path.join(TEST_DIR, "externals", "chromedriver_win32", "chromedriver.exe")
    elif is_linux():
        return os.path.join(TEST_DIR, "externals", "chromedriver_linux64", "chromedriver")
    elif is_macos():
        return os.path.join(TEST_DIR, "externals", "chromedriver_mac64", "chromedriver")
    else:
        print("OS not supported")
        return None

@pytest.fixture()
def firefox_driver():
    if is_windows():
        return os.path.join(TEST_DIR, "externals", "geckodriver_win32", "geckodriver.exe")
    else:
        print("OS not supported")
        return None

@pytest.fixture()
def launch_v1_chrome(hackathon_app_v1, chrome_driver):
    browser = webdriver.Chrome(chrome_driver)
    browser.get(hackathon_app_v1)
    opened_browsers.append(browser)
    return browser

@pytest.fixture()
def launch_v1_firefox(hackathon_app_v1, firefox_driver):
    browser = webdriver.Firefox(executable_path=firefox_driver)
    browser.get(hackathon_app_v1)
    opened_browsers.append(browser)
    return browser

@pytest.fixture
def launch_app(request):
    return request.getfixturevalue(request.param)

@pytest.fixture(autouse=True)
def quit_browsers():
    yield
    for browser in opened_browsers:
        browser.quit()
        opened_browsers.remove(browser)

def is_windows() -> bool:
    system = platform.system()
    return 'Windows' in system

def is_macos() -> bool:
    system = platform.system()
    return 'Darwin' in system

def is_linux() -> bool:
    system = platform.system()
    return 'Linux' in system