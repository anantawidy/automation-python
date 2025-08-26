import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD, INVALID_USERNAME, INVALID_PASSWORD

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    expect(page).to_have_url(BASE_URL + "inventory.html")

def test_unsuccessful_login_invalid_username(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    expect(login_page.get_error()).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_unsuccessful_login_invalid_password(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login(USERNAME, INVALID_PASSWORD)
    expect(login_page.get_error()).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_unsuccessful_login_both_invalid(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login("invalid_user", "invalid_pass")
    expect(login_page.get_error()).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_unsuccessful_login_empty_fields(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.click(LoginPage.LOGIN_BUTTON)
    expect(login_page.get_error()).to_contain_text("Epic sadface: Username is required")

def test_unsuccessful_login_special_chars(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login("user!@#", "validPassword")
    expect(login_page.get_error()).to_contain_text("Epic sadface")

def test_unsuccessful_login_sql_injection(page):
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login("' OR '1'='1", "' OR '1'='1")
    expect(login_page.get_error()).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )