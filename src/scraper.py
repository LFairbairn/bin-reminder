from playwright.sync_api import sync_playwright

def scrape_bin_schedule(playwright, url, postcode, address):
    browser, page = open_browser(playwright, url)
    enter_postcode(page, postcode)
    select_address(page, address)
    extract_bin_data(page)
    browser.close()

def open_browser(playwright, url):
    #opens browser and navigates to url
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    return browser, page

def enter_postcode(page, postcode):
    #Fill in postcode and click search
    page.fill("#dform_widget_ps_45M3LET8_txt_postcode", postcode)
    page.wait_for_timeout(2000)
    page.click("#dform_widget_ps_3SHSN93_searchbutton")
    page.wait_for_timeout(2000)

def select_address(page, address):
    #Click dropdown and select address
    page.click("#select2-dform_widget_ps_3SHSN93_id-container")
    page.wait_for_timeout(1000)
    page.click(f".select2-results__option:has-text('{address}')")
    page.wait_for_timeout(4000)

def extract_bin_data(page):
    rows = page.locator("#dform_widget_table_tab_collections .dform_tr").all()
    print(len(rows))
    for row in rows[1:]:
        date = row.locator("[data-name='date']").inner_text()
        colour = row.locator("[data-name='colour'] img").get_attribute("alt")
        bin_type = row.locator("[data-name='type']").inner_text()
        print(date, colour, bin_type)



with sync_playwright() as playwright:
    scrape_bin_schedule(playwright, "https://fife.portal.uk.empro.verintcloudservices.com/site/fife/request/bin_calendar", "KY2 6ZS", "54 Sir Thomas Elder Way")

