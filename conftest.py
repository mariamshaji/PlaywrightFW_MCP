from collections.abc import Iterator

import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from utils.config import get_browser_name, is_headless


@pytest.fixture
def browser() -> Iterator[Browser]:
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, get_browser_name())
        instance = browser_type.launch(headless=is_headless())
        yield instance
        instance.close()


@pytest.fixture
def page(browser: Browser) -> Iterator[Page]:
    context = browser.new_context()
    test_page = context.new_page()
    yield test_page
    context.close()
