from playwright.sync_api import Page

class AmazonHomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto('https://www.amazon.com')

    def search_product(self, product_name: str):
        self.page.fill('#twotabsearchtextbox', product_name)
        self.page.click('#nav-search-submit-button')
