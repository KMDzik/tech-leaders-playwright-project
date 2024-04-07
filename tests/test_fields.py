from playwright.sync_api import Playwright, sync_playwright, expect


def test_check_main_search(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.esky.pl/")
    page.get_by_test_id("uc-accept-all-button").click()
    page.get_by_role("textbox", name="Miejsce wylotu").click()
    page.get_by_role("textbox", name="Miejsce wylotu").fill("Warszawa")
    page.get_by_role("link", name="Warszawa - wszystkie lotniska").click()
    page.get_by_role("textbox", name="Miejsce przylotu").click()
    page.get_by_role("textbox", name="Miejsce przylotu").fill("Paryż, Francja")
    page.get_by_role("link", name="Paryż - wszystkie lotniska").click()
    page.get_by_role("link", name="7", exact=True).click()
    page.get_by_role("link", name="10", exact=True).click()
    page.get_by_role("link", name="Gotowe").click()
    page.get_by_role("button", name="").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_check_main_search(playwright)


# def test_get_started_link(page: Page):
  # page.goto("https://playwright.dev/")

    # Click the get started link.
   # page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
   # expect(page.get_by_role("heading", name="Installation")).to_be_visible()