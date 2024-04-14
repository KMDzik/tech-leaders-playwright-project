from playwright.sync_api import Page, sync_playwright
from pages.main_search import MainSearchPage


def test_check_main_search():

    # Dlaczego nie mogłam zaimportować klasy

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        main_search_page = MainSearchPage(page)
        main_search_page.open_esky()
        main_search_page.accept_cookies()
        main_search_page.search_departure("WAW")


        main_search_page.departure_airport_list()
        # TypeError: 'Locator' object is not callable

        main_search_page.search_arrival("NFC")

        # main_search_page.arrival_airport_list()
        # TypeError: 'Locator' object is not callable

        main_search_page.set_departure_date()

        main_search_page.return_date()

        page.pause()
        browser.close()

