from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = 'input[data-test="username"]'
    PASSWORD_INPUT = 'input[data-test="password"]'
    LOGIN_BUTTON   = 'input[data-test="login-button"]'
    ERROR_MESSAGE  = '[data-test="error"]'

    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error(self):
        return self.get_locator(self.ERROR_MESSAGE)
