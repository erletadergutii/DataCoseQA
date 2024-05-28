from playwright.sync_api import Page

class AmazonSearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def select_first_product(self):
        self.page.click('.a-size-mini a')
