from playwright.sync_api import Page


class SauceDemoLoginPage:
    URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page) -> None:
        self._page = page
        self._username_input = page.get_by_placeholder("Username")
        self._password_input = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")

    def open(self) -> None:
        self._page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()

    def get_current_url(self) -> str:
        return self._page.url
