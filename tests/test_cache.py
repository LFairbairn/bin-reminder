import pytest
from datetime import date
from src.cache import set_schedule, get_schedule, generate_cache_key, redis_client, CACHE_TTL
from src.models import BinCollection, BinColour

#Integration test for checking Redis integrates properly with the external service. 

def test_cache_store_and_retrieve():
    test_postcode = "TEST123"
    test_address = "1 TEST ROAD"

    #A list with BinCollection objects to test
    test_collections = [BinCollection(bin_date=date(2026, 2, 20), colour=BinColour.GREEN, bin_type='Cans and Plastics'),
    BinCollection(bin_date=date(2026, 2, 27), colour=BinColour.BLUE, bin_type='Landfill')]
    
    # Store it
    set_schedule(test_postcode, test_address, test_collections, CACHE_TTL)
    print('Stored!')

    # Retrieve it
    result = get_schedule(test_postcode, test_address)
    print(f'Retrieved: {result}')

    assert len(result) == 2
    assert result[0].colour == BinColour.GREEN
    assert result[1].bin_type == "Landfill"

    redis_client.delete(generate_cache_key(test_postcode, test_address))
