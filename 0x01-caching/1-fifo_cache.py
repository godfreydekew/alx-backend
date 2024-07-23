#!/usr/bin/env python3
"""1. FIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements FIFO cache replacement method"""
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key, value = list(self.cache_data.items())[0]
                del self.cache_data[key]
                print("DISCARD: {}".format(key))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
