from playwright.sync_api import Page

class AmazonProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_basket(self):
        self.page.click('#add-to-cart-button')
