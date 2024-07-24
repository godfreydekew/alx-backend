#!/usr/bin/python3
"""LFU Caching"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Defines Least frequently used caching methods"""

    def __init__(self):
        super().__init__()
        self.count_dict = OrderedDict()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.count_dict.keys():
                self.count_dict[key] += 1
                self.count_dict.move_to_end(key)
            else:
                self.count_dict[key] = 0
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_key = min(self.count_dict, key=self.count_dict.get)
                print("DISCARD: {}".format(min_key))
                del self.count_dict[min_key]
                del self.cache_data[min_key]

    def get(self, key):
        """ Get an item by key
        """
        if key in self.count_dict.keys():
            self.count_dict[key] += 1
            self.count_dict.move_to_end(key)
        return self.cache_data.get(key)
