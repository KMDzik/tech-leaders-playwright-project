from playwright.sync_api import Page


class CalendarPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.selected_date = page.get_by_role("link", name="24")

    def select_day_from_calendar(self) -> None:
        self.selected_date.click()
