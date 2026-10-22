from playwright.sync_api import Page

from pages.saucedemo_login_page import SauceDemoLoginPage


def test_saucedemo_login_tc(page: Page) -> None:
    login_page = SauceDemoLoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.get_current_url() == SauceDemoLoginPage.INVENTORY_URL