from playwright.sync_api import sync_playwright

from pages.main_search import MainSearchPage


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

        main_search_page.click_search_btn_and_check_url()

        browser.close()
