#!/usr/bin/env python3
""" This module defines a pagination feature. """


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ Computes the range of a query results. """
    limit = math.floor(page * page_size)
    offset = limit - page_size
    return (offset, limit)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return data from a specific range computed using the 
        current page and the page size attributes.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        (offset, limit) = index_range(page, page_size)

        if offset > len(self.dataset()) or limit > len(self.dataset()):
            return []
        return self.dataset()[offset:limit]