#!/usr/bin/python3
"""LRU Caching"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    "Defines Least recently used Caching"
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark as recently used
            return self.cache_data[key]
        return None
