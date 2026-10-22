from playwright.sync_api import Page


class BingPage:
    HOME_URL = "https://www.bing.com/"
    SAFESEARCH_URL = "https://www.bing.com/account/general?ru"
    EXPECTED_TITLE = "Search - Microsoft Bing"

    def __init__(self, page: Page) -> None:
        self._page = page
        self._strict_radio = page.get_by_role("radio", name="Strict")

    def open_homepage(self) -> None:
        self._page.goto(self.HOME_URL)

    def open_safesearch_settings(self) -> None:
        self._page.goto(self.SAFESEARCH_URL)

    def get_title(self) -> str:
        return self._page.title()

    def enable_strict_safesearch(self) -> None:
        self._strict_radio.check()

    def is_strict_safesearch_enabled(self) -> bool:
        return self._strict_radio.is_checked()
