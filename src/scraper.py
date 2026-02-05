from playwright.sync_api import sync_playwright

def run(playwright, url, postcode, address):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.fill("#dform_widget_ps_45M3LET8_txt_postcode", postcode)
    page.wait_for_timeout(3000)
    page.click("#dform_widget_ps_3SHSN93_searchbutton")
    page.wait_for_timeout(3000)
    page.click("#select2-dform_widget_ps_3SHSN93_id-container")
    page.wait_for_timeout(1000)
    page.click(f".select2-results__option:has-text('{address}')")
    page.wait_for_timeout(5000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright, "https://fife.portal.uk.empro.verintcloudservices.com/site/fife/request/bin_calendar", "KY1 1HH", "90 Alexandra Street")