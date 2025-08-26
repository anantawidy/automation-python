import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from utils.config import BASE_URL, USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE


def test_successful_checkout_with_valid_items(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    confirmation_page = ConfirmationPage(page)

    # Login
    login_page.goto(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    # Add items
    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    inventory_page.go_to_cart()

    # Checkout
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.finish_checkout()

    # Verify confirmation
    expect(confirmation_page.get_confirmation_header()).to_contain_text("Thank you for your order!")
    expect(confirmation_page.get_confirmation_text()).to_contain_text("Your order has been dispatched")

def test_checkout_with_no_items(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.goto(BASE_URL)
    login_page.login("standard_user", "secret_sauce")

    # Cart without items
    inventory_page.go_to_cart()
    expect(cart_page.get_cart_items()).to_have_count(0)

    # Try checkout
    cart_page.proceed_to_checkout()

    # Error (checkout without items will usually fail)
    error = page.locator('.error-message-container')
    expect(error).to_be_visible()
