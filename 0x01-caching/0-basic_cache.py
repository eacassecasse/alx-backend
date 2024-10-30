#!/usr/bin/env python3
""" This module defines a model BasicCache. """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Definition of a basic caching system. """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign a value to a cache item. """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value of a cached item. """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
