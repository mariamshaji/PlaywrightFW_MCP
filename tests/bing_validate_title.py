from playwright.sync_api import Page

from pages.bing_page import BingPage


def test_navigate_to_bing_and_verify_the_title_of_the_webpage(page: Page) -> None:
    bing_page = BingPage(page)
    bing_page.open_homepage()

    assert bing_page.get_title() == BingPage.EXPECTED_TITLE