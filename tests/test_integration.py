import pytest
from playwright.sync_api import sync_playwright
from src.scraper import scrape_bin_schedule
from src.models import BinCollection, BinColour

COUNCIL_URL = "https://fife.portal.uk.empro.verintcloudservices.com/site/fife/request/bin_calendar"

@pytest.mark.integration
def test_scrape_real_council_website():
    """Integration test - hits the real council website to verify scraper works"""
    postcode = "KY1 1HH"
    address = "92"

    with sync_playwright() as playwright:
        collections = scrape_bin_schedule(playwright, COUNCIL_URL, postcode, address)

    # Verify we got results (council provides ~7 weeks of data)
    assert len(collections) > 0

    # Verify each collection has correct structure
    # Council returns types like "Cans and Plastics / Green Bin" so we check for partial match
    expected_types = ["Cans and Plastics", "Food and Garden Waste", "Landfill", "Paper and Cardboard"]

    for collection in collections:
        assert isinstance(collection, BinCollection)
        assert collection.bin_date is not None
        assert isinstance(collection.colour, BinColour)
        assert any(expected in collection.bin_type for expected in expected_types), \
            f"Unexpected bin type: {collection.bin_type}"

    # Verify we have a reasonable number of collections (at least 4 weeks worth)
    assert len(collections) >= 4
