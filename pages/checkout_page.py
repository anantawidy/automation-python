from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRSTNAME_INPUT = 'input[data-test="firstName"]'
    LASTNAME_INPUT  = 'input[data-test="lastName"]'
    POSTALCODE_INPUT= 'input[data-test="postalCode"]'
    CONTINUE_BUTTON = 'input[data-test="continue"]'
    FINISH_BUTTON   = 'button[data-test="finish"]'

    def fill_checkout_info(self, firstname, lastname, postal):
        self.fill(self.FIRSTNAME_INPUT, firstname)
        self.fill(self.LASTNAME_INPUT, lastname)
        self.fill(self.POSTALCODE_INPUT, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
