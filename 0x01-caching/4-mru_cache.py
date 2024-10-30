#!/usr/bin/env python3
""" This module defines a MRUCache model. """

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a MRU Caching System. """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assigns a value to a cache item using MRU. """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """ Retrieves a cached item. """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
