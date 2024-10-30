#!/usr/bin/env python3
""" This module defines a FIFOCache model. """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a FIFO Caching System. """
    
    def __init__(self):
        super().__init__()


    def put(self, key, item):
        """ Assigns a value to a cache item using FIFO. """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = list(self.cache_data)[0]
                print(f"DISCARD: {discarded}")
                del self.cache_data[discarded]
            


    def get(self, key):
        """ Retrieves a cached item. """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None