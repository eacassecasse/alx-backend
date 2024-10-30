#!/usr/bin/env python3
""" This module defines a LFUCache model. """

from collections import OrderedDict
from functools import wraps
from typing import Callable
from base_caching import BaseCaching


def call_count(method: Callable) -> Callable:
    """ Keeps track of usage frequency. """
    @wraps(method)
    def counter(self, key):
        """ Increment the usage frequency when a cached item is acessed. """
        self.usage_frequency[key] += 1
        return method(self, key)
    return counter


class LFUCache(BaseCaching):
    """ Defines a LFU Caching System. """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = {}

    def put(self, key, item):
        """ Assigns a value to a cache item using LFU. """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.usage_frequency[key] = 1
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_frequent = [
                k for k, v in self.usage_frequency.items()
                if v == min(self.usage_frequency.values())
                ]
            if len(least_frequent) <= 1:
                discarded, _ = self.cache_data.pop(least_frequent[0])
            else:
                discarded, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded}")

    @call_count
    def get(self, key):
        """ Retrieves a cached item. """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
