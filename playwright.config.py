from playwright.sync_api import sync_playwright


def get_browser():
    """
    Initializes and returns a Playwright browser instance
    """
    with sync_playwright() as p:
        return p.chromium.launch(headless=False)  # Set to True for headless mode


config = {
    'browser': get_browser,
    'base_url': 'https://esky.pl',
    'timeout': 30000
}
