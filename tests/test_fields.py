from playwright.sync_api import Page, sync_playwright

from pages.main_search import MainSearchPage
import time

def test_check_main_search():

    # Dlaczego nie mogłam zaimportować klasy playwright.config.py

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        main_search_page = MainSearchPage(page)
        main_search_page.open_esky()
        main_search_page.accept_cookies()
        main_search_page.search_departure("WAW")

        main_search_page.search_arrival("FNC")
        main_search_page.set_departure_date()

        main_search_page.set_return_date()
        time.sleep(20)
        browser.close()

