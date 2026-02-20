from fastapi import FastAPI, HTTPException
from playwright.sync_api import sync_playwright
from .cache import get_schedule, set_schedule, CACHE_TTL, clear_cache
from .scraper import scrape_bin_schedule
import re

COUNCIL_URL = "https://fife.portal.uk.empro.verintcloudservices.com/site/fife/request/bin_calendar"
POSTCODE_PATTERN = r"(?i)^(KY|DD|FK)[0-9]{1,2}\s?[0-9][A-Z]{2}$"

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/schedule")
def get_bin_schedule(postcode: str, address: str):
    if not re.match(POSTCODE_PATTERN, postcode):
        raise HTTPException(
            status_code=400,
            detail="Invalid postcode. Must be a Fife area postcode (KY, DD, or FK)"
        )
    if not address:
        raise HTTPException(
            status_code=400,
            detail="Address is required"
        )
    # Check cache
    cached = get_schedule(postcode, address)
    if cached:
        return {"collections": cached, "source": "cache"}
    
    #cache miss - scrape the council website
    with sync_playwright() as playwright:
        collections = scrape_bin_schedule(playwright, COUNCIL_URL, postcode, address)

    #store in cache
    set_schedule(postcode, address, collections, CACHE_TTL)

    return {"collections": collections, "source": "scraped"}

@app.delete("/cache")
def delete_cache():
    clear_cache()
    return {"message": "Cache cleared successfully"}
