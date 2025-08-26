from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = 'button[data-test="checkout"]'
    CART_ITEMS      = '.cart_item'

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def get_cart_items(self):
        return self.get_locator(self.CART_ITEMS)