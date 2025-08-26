from pages.base_page import BasePage

class ConfirmationPage(BasePage):
    COMPLETE_HEADER = '.complete-header'
    COMPLETE_TEXT   = '.complete-text'

    def get_confirmation_header(self):
        return self.get_locator(self.COMPLETE_HEADER)

    def get_confirmation_text(self):
        return self.get_locator(self.COMPLETE_TEXT)
