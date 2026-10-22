from playwright.sync_api import Page

from pages.bing_page import BingPage


def test_go_to_bing_and_enable_strict_safesearch(page: Page) -> None:
    bing_page = BingPage(page)
    bing_page.open_safesearch_settings()
    bing_page.enable_strict_safesearch()

    assert bing_page.is_strict_safesearch_enabled()