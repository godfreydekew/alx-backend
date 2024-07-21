#!/usr/bin/env python3
'''
1. Simple pagination
'''
import csv
import math
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


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
        """Retrieves each page information"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)
        my_list = self.dataset()
        if start_index < len(my_list) or end_index < len(my_list):
            new_list = my_list[start_index:]
            return new_list[0:page_size]
        else:
            return []
