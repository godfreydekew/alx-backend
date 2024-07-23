#!/usr/bin/env python3
"""0. Basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements basic CAching and defines super class functions"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
