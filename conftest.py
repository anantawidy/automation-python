class BasePage:
    def __init__(self, page):
        self.page = page

    async def navigate(self, url: str):
        await self.page.goto(url)

    async def click(self, selector: str):
        await self.page.click(selector)

    async def fill(self, selector: str, value: str):
        await self.page.fill(selector, value)

    async def get_text(self, selector: str) -> str:
        return await self.page.text_content(selector)

    async def is_visible(self, selector: str) -> bool:
        return await self.page.is_visible(selector)
