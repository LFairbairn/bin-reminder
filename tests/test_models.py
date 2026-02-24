import pytest
from datetime import date
from src.models import BinColour, BinCollection

def test_bin_colour_values():
    #Test that all expected colours exist
    assert BinColour.GREEN.value == "green"
    assert BinColour.BROWN.value == "brown"
    assert BinColour.BLUE.value == "blue"
    assert BinColour.GREY.value == "grey"

def test_bin_collection_valid():
    #Test creating a valid BinCollection
    collection = BinCollection(
        bin_date=date(2026, 3, 15), 
        colour=BinColour.GREEN, 
        bin_type="General Waste"
     )
    assert collection.bin_date == date(2026,3,15)
    assert collection.colour == BinColour.GREEN

def test_bin_collection_invalid_colour():
    #Test that invalid colour raises error
    with pytest.raises(ValueError):
        BinCollection(
            bin_date=date(2026, 3, 15),
            colour="purple", #not a valid BinColour
            bin_type="General Waste"
        )