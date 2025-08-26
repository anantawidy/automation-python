class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def get_locator(self, selector: str):
        return self.page.locator(selector)
