import pytest
import time

def test_launch_and_close_app(launch_v1_chrome):
    browser = launch_v1_chrome
    time.sleep(5)
    browser.quit()

@pytest.mark.parametrize(
    "launch_app", [
        'launch_v1_chrome',
    ],
    indirect=['launch_app']
)
def test_login_page_UI_elements(launch_app):
    browser = launch_app
    assert "ACME demo app" in browser.title