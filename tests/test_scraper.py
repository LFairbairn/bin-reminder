from unittest.mock import MagicMock
from datetime import date
from src.scraper import extract_bin_data
from src.models import BinColour

def test_extract_bin_data():
    #Create mock page
    mock_page = MagicMock()

    #Create mock rows (header + 1 data row)
    mock_header_row = MagicMock()
    mock_data_row = MagicMock()

    #Create separate mocks for each locator call
    mock_date_locator = MagicMock()
    mock_date_locator.inner_text = MagicMock(return_value="Monday, March 15, 2026")

    mock_colour_locator = MagicMock()
    mock_colour_locator.get_attribute = MagicMock(return_value="Green")

    mock_type_locator = MagicMock()
    mock_type_locator.inner_text = MagicMock(return_value="Cans and Plastics")

    #Make row.locator() return different mocks based on selector
    def locator_side_effect(selector):
        if "date" in selector:
            return mock_date_locator
        elif "colour" in selector:
            return mock_colour_locator
        elif "type" in selector:
            return mock_type_locator
        
    mock_data_row.locator.side_effect = locator_side_effect
        
    #Make page.locator().all() return our mock rows
    mock_page.locator.return_value.all.return_value = [mock_header_row, mock_data_row]

    #Call the function
    result = extract_bin_data(mock_page)

    #Verify
    assert len(result) == 1
    assert result[0].bin_date == date(2026, 3 , 15)
    assert result[0].colour == BinColour.GREEN
    assert result[0].bin_type == "Cans and Plastics"
