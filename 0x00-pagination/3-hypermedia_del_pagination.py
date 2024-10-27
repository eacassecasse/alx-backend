#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return indexed data and hypermedias from a specific range computed
        using the current index and the page size attributes.
        """
        
        dataset = self.indexed_dataset()
        keys = list(dataset.keys())
        total_items = len(dataset)
        start_index = index

        if not index or index not in keys:
            start_index = next((k for k in keys
                if k >= (index or 0)), keys[0] if keys else 0)

        if index:
            assert 0 <= index <= total_items

        cur_index = keys.index(start_index)
        count = 0
        data = []

        while count < page_size and cur_index < len(keys):
            key = keys[cur_index]
            if key in dataset:
                data.append(dataset[key])
                count += 1
            cur_index += 1

        next_index = keys[cur_index] if cur_index < len(keys) else None
            
        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(data),
                "data": data
                }
