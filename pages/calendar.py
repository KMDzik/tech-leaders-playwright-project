from playwright.sync_api import Page


class CalendarPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.selected_date = page.locator("a[normalize-space()='24']")
        self.today_date = page.locator(".ui-datepicker-days-cell-over.selected-today.ui-datepicker-today")
        self.next_month_arrow = page.locator(".ui-icon.ui-icon.ui-icon-circle-triangle-e")

    def select_today_from_calendar(self) -> None:
        self.today_date.wait_for(state="visible")
        self.today_date.click()
    
    def go_to_next_month(self) -> None:
        self.next_month_arrow.wait_for(state="visible")
        self.next_month_arrow.click()

    def select_x_day_next_month(self, day: str) -> None:
        third_day_next_month = self.page.get_by_text(f"{day}", exact=True)
        third_day_next_month.wait_for(state="visible")
        third_day_next_month.click()
