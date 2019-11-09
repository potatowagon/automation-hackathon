import pytest
import time

from selenium import webdriver

def test_launch_and_close_app(launch_v1_chrome):
    browser = launch_v1_chrome
    time.sleep(5)
    browser.quit()

def test_login_page_UI_elements(launch_v1_chrome):
    