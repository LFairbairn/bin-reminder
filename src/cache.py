import redis
import json
from .models import BinCollection

#constant calculation for 70 days converted to seconds, days x hours x minutes x seconds
CACHE_TTL = 70 * 24 * 60 * 60

redis_client = redis.Redis(host='localhost', port=6379, db=0)

#generates cache key for redis
def generate_cache_key(postcode, address):
    key = f"bin_schedule:{postcode}:{address}"
    return key

#stores/sets data with expiration time and converts to json for every collection
def set_schedule(postcode, address, collections, ttl):
    key = generate_cache_key(postcode, address)
    json_data = json.dumps([c.model_dump(mode="json") for c in collections])
    redis_client.set(key, json_data, ex=ttl)

#retrieves data from Redis if key exists, returns None if not found
def get_schedule(postcode, address):
    key = generate_cache_key(postcode, address)
    data = redis_client.get(key)
    if data is None:
        return None
    parsed = json.loads(data)
    return [BinCollection(**item) for item in parsed]
    