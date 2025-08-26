from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_ADD    = 'button[data-test="add-to-cart-sauce-labs-backpack"]'
    BIKE_LIGHT_ADD  = 'button[data-test="add-to-cart-sauce-labs-bike-light"]'
    CART_LINK       = 'a.shopping_cart_link'

    def add_backpack(self):
        self.click(self.BACKPACK_ADD)

    def add_bike_light(self):
        self.click(self.BIKE_LIGHT_ADD)

    def go_to_cart(self):
        self.click(self.CART_LINK)
