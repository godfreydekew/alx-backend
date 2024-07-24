#!/usr/bin/python3
"""#!/usr/bin/python3 """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    "Defines Most recently used Caching"

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_recently_used_key = list(self.cache_data.keys())[-2]
                del self.cache_data[most_recently_used_key]
                print("DISCARD: {}".format(most_recently_used_key))

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
