#!/usr/bin/env python3
"""0x01. Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO cache replacement method"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.lifo_list = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.lifo_list.append(key)
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                pop_item = self.lifo_list.pop(-2)
                del self.cache_data[pop_item]
                print("DISCARD: {}".format(pop_item))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
