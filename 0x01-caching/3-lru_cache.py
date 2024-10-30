#!/usr/bin/env python3
""" This module defines a LRUCache model. """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines a LRU Caching System. """
    
    def __init__(self):
        super().__init__()


    def put(self, key, item):
        """ Assigns a value to a cache item using LRU. """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                rank = 0
                keys = list(self.cache_data)
                ranks = {}

                for key in keys:
                    ranks[key] = rank
                    rank += 1

                discarded = keys[ranks[min(ranks, key=ranks.get)]]
                print(f"DISCARD: {discarded}")
                del self.cache_data[discarded]
            


    def get(self, key):
        """ Retrieves a cached item. """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None