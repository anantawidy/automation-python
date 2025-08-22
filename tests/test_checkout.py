import pytest
from playwright.sync_api import Page, expect

def test_successful_checkout_with_valid_items(page: Page):
    # Navigate to the URL
    page.goto("https://www.saucedemo.com/")

    # Log in as a valid user
    page.fill('input[placeholder="Username"]', 'standard_user')
    page.fill('input[placeholder="Password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    # Add items to the cart
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')

    # Proceed to checkout
    page.click('a.shopping_cart_link')
    page.click('button[data-test="checkout"]')

    # Fill in checkout information
    page.fill('input[data-test="firstName"]', 'John')
    page.fill('input[data-test="lastName"]', 'Doe')
    page.fill('input[data-test="postalCode"]', '12345')
    page.click('input[data-test="continue"]')

    # Finish checkout
    page.click('button[data-test="finish"]')

    # Verify confirmation message
    confirmation_message = page.locator('.complete-header')
    expect(confirmation_message).to_contain_text("Thank you for your order!")

    order_confirmation = page.locator('.complete-text')
    expect(order_confirmation).to_contain_text("Your order has been dispatched")


def test_checkout_with_no_items(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill('input[data-test="username"]', 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')

    # Ensure cart is empty
    page.click('a.shopping_cart_link')
    expect(page.locator('.cart_item')).to_have_count(0)

    # Proceed to checkout
    page.click('button[data-test="checkout"]')

    # Verify error message
    error = page.locator('.error-message-container')
    expect(error).to_be_visible()