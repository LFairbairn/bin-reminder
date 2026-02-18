from enum import Enum
from pydantic import BaseModel
from datetime import date, datetime

class BinColour(Enum):
    GREEN = "green"
    BROWN = "brown"
    BLUE = "blue"
    GREY = "grey"

class BinCollection(BaseModel):
    bin_date: date
    colour: BinColour
    bin_type: str

class BinScheduleResponse(BaseModel):
    address: str
    collection_date: date
    days_until: int
    bin_colour: BinColour
    bin_type: str
    cached_at: datetime


class ScraperError(Exception):
    """Base exception for scraper errors"""
    pass


