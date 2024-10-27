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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return data and hypermedias from a specific range computed using the 
        current page and the page size attributes.
        """
        result = {
            "page_size": 0,
            "page": 0,
            "data": [],
            "next_page": None,
            "prev_page": None,
            "total_pages": 0
        }

        dataset_size = len(self.dataset())

        if dataset_size > 0:
            total_pages = math.ceil(dataset_size / page_size)
            data = self.get_page(page, page_size)
            result["page"] = page
            result["total_pages"] = total_pages
            result["data"] = data

            if data:
                result["page_size"] = len(data)
            if page > 1:
                result["prev_page"] = page - 1
            if page >= 1 and page < total_pages:
                result["next_page"] = page + 1

        return result
