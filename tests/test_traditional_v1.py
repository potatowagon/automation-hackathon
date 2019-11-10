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
    assert "index.html" == logo.a.get('href')
    assert "img/logo-big.png" == logo.img.get('src')
    assert "Login Form" in browser.find_element_by_class_name("auth-header").get_attribute("innerText")

    forms = browser.find_elements_by_class_name("form-group")
    username_form = BeautifulSoup(forms[0].get_attribute("innerHTML"), "html.parser")
    assert "Username" == username_form.label.string
    assert "form-control" == username_form.input.get('class')[0]
    assert "Enter your username" == username_form.input.get('placeholder')
    assert "text" == username_form.input.get('type')
    assert "pre-icon os-icon os-icon-user-male-circle" == ' '.join(username_form.div.get('class'))

    password_form = BeautifulSoup(forms[1].get_attribute("innerHTML"), "html.parser")
    assert "Password" == password_form.label.string
    assert "form-control" == password_form.input.get('class')[0]
    assert "Enter your password" == password_form.input.get('placeholder')
    assert "password" == password_form.input.get('type')
    assert "pre-icon os-icon os-icon-fingerprint" == ' '.join(password_form.div.get('class'))

    buttons_w = browser.find_element_by_class_name("buttons-w")
    login_button = buttons_w.find_element_by_id("log-in")
    assert "button" == login_button.get_attribute('tagName').lower()
    assert "Log In" == login_button.get_attribute('innerText')

    remember_me_cb = buttons_w.find_element_by_class_name("form-check-inline")
    assert "checkbox" == remember_me_cb.find_element_by_class_name("form-check-input").get_attribute("type")
    assert "Remember Me" == remember_me_cb.get_attribute("innerText")

    icons = buttons_w.find_elements_by_tag_name("a")
    icons_img_src = [
        "img/social-icons/twitter.png",
        "img/social-icons/facebook.png",
        "img/social-icons/linkedin.png",
    ]
    for icon in icons:
        assert icon.get_attribute('href').endswith("#")
        icon_img_src = icon.find_element_by_tag_name("img").get_attribute("src").replace("https://demo.applitools.com/", "")
        assert icon_img_src in icons_img_src
        icons_img_src.remove(icon_img_src)
    assert icons_img_src == []

@pytest.mark.parametrize(
    "launch_app", [
        'launch_v1_chrome',
        'launch_v1_firefox'
    ],
    indirect=['launch_app']
)
def test_data_driven(launch_app):
    browser = launch_app
    username_input = browser.find_element_by_id("username")
    password_input = browser.find_element_by_id("password")
    login_button = browser.find_element_by_id("log-in")

    def test_login_fail(username, password, expected_error_msg):
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        assert expected_error_msg == browser.find_element_by_xpath("//*[starts-with(@id,'random_id_')]").get_attribute("innerText")
        username_input.clear()
        password_input.clear()

    test_login_fail("", "", "Both Username and Password must be present")
    test_login_fail("boop", "", "Password must be present")
    test_login_fail("", "boop", "Username must be present")

