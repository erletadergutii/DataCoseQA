from playwright.sync_api import Page

class AmazonBasketPage:
    def __init__(self, page: Page):
        self.page = page

    def update_quantity(self, quantity: int):
        self.page.select_option('select[name="quantity"]', str(quantity))

    def get_quantity(self) -> int:
        return int(self.page.input_value('select[name="quantity"]'))
