from playwright.sync_api import Page


class DatePickerPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.departure_date = page.locator("//a[normalize-space()=\"24\"]")

    def set_select_day(self) -> None:
        self.departure_day.click()

