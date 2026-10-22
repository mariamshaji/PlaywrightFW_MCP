import os


SUPPORTED_BROWSERS = {"chromium", "firefox", "webkit"}


def get_browser_name() -> str:
    browser_name = os.getenv("PLAYWRIGHT_BROWSER", "chromium").lower()
    if browser_name not in SUPPORTED_BROWSERS:
        supported = ", ".join(sorted(SUPPORTED_BROWSERS))
        raise ValueError(f"Unsupported PLAYWRIGHT_BROWSER '{browser_name}'. Choose from: {supported}.")
    return browser_name


def is_headless() -> bool:
    return os.getenv("PLAYWRIGHT_HEADLESS", "true").strip().lower() not in {"0", "false", "no"}
