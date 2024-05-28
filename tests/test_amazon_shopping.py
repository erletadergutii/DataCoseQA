import pytest
from playwright.sync_api import sync_playwright
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_search_results_page import AmazonSearchResultsPage
from pages.amazon_product_page import AmazonProductPage
from pages.amazon_basket_page import AmazonBasketPage

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_amazon_shopping(page):
    amazon_home_page = AmazonHomePage(page)
    amazon_search_results_page = AmazonSearchResultsPage(page)
    amazon_product_page = AmazonProductPage(page)
    amazon_basket_page = AmazonBasketPage(page)

    amazon_home_page.goto()
    amazon_home_page.search_product("laptop")
    amazon_search_results_page.select_first_product()
    amazon_product_page.add_to_basket()
    page.goto('https://www.amazon.com/gp/cart/view.html')
    amazon_basket_page.update_quantity(2)

    assert amazon_basket_page.get_quantity() == 2
