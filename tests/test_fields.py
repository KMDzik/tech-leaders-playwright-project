from playwright.sync_api import Page, sync_playwright

from pages.date_picker import DatePickerPage
from pages.main_search import MainSearchPage


def test_check_main_search():

    # Dlaczego nie mogłam zaimportować klasy playwright.config.py

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        main_search_page = MainSearchPage(page)
        date_picker_page = DatePickerPage(page)
        main_search_page.open_esky()
        main_search_page.accept_cookies()
        main_search_page.search_departure("WAW")
        # nie przeładowuje się lista
        # main_search_page.search_arrival("FNC")
        date_picker_page.set_departure_date()
        date_picker_page.return_date()

        browser.close()

