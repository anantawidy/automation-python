import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[placeholder="Username"]', 'standard_user')
    page.fill('input[placeholder="Password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_unsuccessful_login_invalid_username(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[placeholder="Username"]', 'invalid_user')
    page.fill('input[placeholder="Password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    error_message = page.locator('h3[data-test="error"]')
    print("🔍 Actual text:", error_message.text_content())
    expect(error_message).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_unsuccessful_login_invalid_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[placeholder="Username"]', 'standard_user')
    page.fill('input[placeholder="Password"]', 'invalid_password')
    page.click('input[type="submit"]')

    error_message = page.locator('h3[data-test="error"]')
    print("🔍 Actual text:", error_message.text_content())
    expect(error_message).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_unsuccessful_login_both_invalid(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[placeholder="Username"]', 'invalid_user')
    page.fill('input[placeholder="Password"]', 'invalid_pass')
    page.click('input[type="submit"]')

    error_message = page.locator('[data-test="error"]')
    print("🔍 Actual text:", error_message.text_content())
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_unsuccessful_login_empty_fields(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.click('input[type="submit"]')

    error_message = page.locator('.error-message-container')
    print("🔍 Actual text:", error_message.text_content())
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Epic sadface: Username is required")

def test_unsuccessful_login_special_chars(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[placeholder="Username"]', 'user!@#')
    page.fill('input[placeholder="Password"]', 'validPassword')
    page.click('input[type="submit"]')

    error_message = page.locator('.error-message-container')
    print("🔍 Actual text:", error_message.text_content())
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Epic sadface")

def test_unsuccessful_login_sql_injection(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[placeholder="Username"]', "' OR '1'='1")
    page.fill('input[placeholder="Password"]', "' OR '1'='1")
    page.click('input[type="submit"]')

    error_message = page.locator('[data-test="error"]')
    print("🔍 Actual text:", error_message.text_content())
    expect(error_message).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )