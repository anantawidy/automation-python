import pytest
from playwright.sync_api import sync_playwright, expect

def test_verify_homepage_loads_successfully(page):
    page.goto("https://www.demoblaze.com/index.html")
    expect(page).to_have_title("STORE")

def test_check_product_categories(page):
    page.goto("https://www.demoblaze.com/index.html")
    categories = page.locator(".list-group-item").all_text_contents()
    assert "Laptops" in categories
    assert "Monitors" in categories
    assert "Phones" in categories

def test_add_product_to_cart(page):
    page.goto("https://www.demoblaze.com/index.html")
    page.click('a:has-text("Laptops")')
    page.click('.card-title a:has-text("Sony vaio i5")')
    alert_message = {}

    # fungsi untuk menangani dialog alert
    def handle_dialog(dialog):
        alert_message["text"] = dialog.message
        dialog.accept()

    # pasang listener sebelum klik
    page.on("dialog", handle_dialog)
    page.click('//a[contains(text(),"Add to cart")]')

    # tunggu sebentar biar alert ketangkap
    page.wait_for_timeout(2000)
    assert alert_message["text"] == "Product added"

def test_view_cart(page):
    page.goto("https://www.demoblaze.com/index.html")
    page.click('a:has-text("Laptops")')
    page.click('.card-title a:has-text("Sony vaio i5")')

    # Tangani dialog dengan context manager (lebih rapi)
    with page.expect_event("dialog") as dialog_info:
        page.click('a:has-text("Add to cart")')

    dialog = dialog_info.value
    assert dialog.message == "Product added"   # ✅ verifikasi isi alert
    dialog.accept()                            # ✅ klik tombol OK pada alert
    page.click("#cartur")
    assert page.url == "https://www.demoblaze.com/cart.html"
    page.wait_for_selector("td:has-text('Sony vaio i5')")
    assert "Sony vaio i5" in page.inner_text("body")

def test_check_login_functionality(page):
    page.goto("https://www.demoblaze.com/index.html")
    page.click('//a[contains(text(),"Log in")]')
    page.fill('//input[@id="loginusername"]', "test")
    page.fill('//input[@id="loginpassword"]', "test")
    page.click('button:has-text("Log in")')
    page.wait_for_selector('text="Welcome test"')
    assert page.url == "https://www.demoblaze.com/index.html"
    assert page.locator('//a[contains(text(),"Welcome test")]').is_visible()

def test_check_product_details(page):
    page.goto("https://www.demoblaze.com/index.html")
    page.click('a:has-text("Laptops")')
    page.click('.card-title a:has-text("Sony vaio i5")')
    assert page.url == "https://www.demoblaze.com/prod.html?idp_=8"
    assert page.locator('.name').text_content() == "Sony vaio i5"
    actual_text = page.locator('//p[contains(text(),"Sony is so confident")]').text_content()
    assert "Sony is so confident that the VAIO S is a superior ultraportable laptop" in actual_text
