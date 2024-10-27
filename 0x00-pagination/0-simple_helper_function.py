#!/usr/bin/env python3
""" This module defines a function named index_range. """

import math


def index_range(page: int, page_size: int) -> tuple:
    """ Computes the range of a query results. """
    limit = math.floor(page * page_size)
    offset = limit - page_size
    return (offset, limit)
