import time

import pytest
from bs4 import BeautifulSoup

def test_launch_and_close_app(launch_v1_chrome):
    browser = launch_v1_chrome
    time.sleep(5)

@pytest.mark.parametrize(
    "launch_app", [
        'launch_v1_chrome',
        'launch_v1_firefox'
    ],
    indirect=['launch_app']
)
def test_login_page_UI_elements(launch_app):
    browser = launch_app
    assert "ACME demo app" in browser.title
    logo = BeautifulSoup(browser.find_element_by_class_name("logo-w").get_attribute("innerHTML"), "html.parser")
    assert logo.a.get('href') == "index.html"
    assert logo.img.get('src') == "img/logo-big.png"
