from playwright.sync_api import sync_playwright
from datetime import datetime
from .models import BinColour, BinCollection, ScraperError

DEFAULT_WAIT_TIME = 1000

def click_and_wait(page, locator: str, wait_time: int = DEFAULT_WAIT_TIME, timeout: int = 30000):
    page.click(locator, timeout=timeout)
    page.wait_for_timeout(wait_time)

def fill_and_wait(page, locator: str, value, wait_time: int = DEFAULT_WAIT_TIME):
    page.fill(locator, value)
    page.wait_for_timeout(wait_time)

def open_browser(playwright, url):
    #opens browser and navigates to url
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    try:
        page.goto(url)
    except Exception:
        raise ScraperError("Could not load council website - check your internet connection")
    return browser, page

def scrape_bin_schedule(playwright, url, postcode, address):
    browser, page = open_browser(playwright, url)
    enter_postcode(page, postcode)
    select_address(page, address)
    collections = extract_bin_data(page)
    browser.close()
    return collections

def enter_postcode(page, postcode):
    #Fill in postcode and click search
    fill_and_wait(page, "#dform_widget_ps_45M3LET8_txt_postcode", postcode)
    click_and_wait(page, "#dform_widget_ps_3SHSN93_searchbutton")

def select_address(page, address):
    #Click dropdown and select address
    click_and_wait(page, "#select2-dform_widget_ps_3SHSN93_id-container")
    try:
        click_and_wait(page, f".select2-results__option:has-text('{address}')", timeout=5000)
    except Exception:
        raise ScraperError("Address not found - check postcode and address are correct")

def extract_bin_data(page):
    #extract rows of bin data and parse data for Pydantic model
    rows = page.locator("#dform_widget_table_tab_collections .dform_tr").all()
    collections = []
    for row in rows[1:]:
        date = row.locator("[data-name='date']").inner_text()
        parsed_date = datetime.strptime(date, "%A, %B %d, %Y").date()
        colour = row.locator("[data-name='colour'] img").get_attribute("alt")
        bin_colour = BinColour(colour.lower())
        bin_type = row.locator("[data-name='type']").inner_text()
        collection = BinCollection(
            bin_date=parsed_date,
            colour=bin_colour,
            bin_type=bin_type
        )
        collections.append(collection)
    return collections