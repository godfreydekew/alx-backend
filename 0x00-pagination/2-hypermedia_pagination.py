#!/usr/bin/env python3
'''
2. Hypermedia pagination
'''
import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ returns a dictionary containing all the information of page"""
        data_set = self.get_page(page, page_size)
        np = None
        prev_page = page - 1 if (page - 1) > 0 else None
        page_c = page + 1
        try:
            np = page_c if len(self.get_page(page_c, page_size)) > 0 else None

        except AssertionError:
            pass

        return {
            "page_size": len(data_set),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": np,
            "prev_page": prev_page,
            "total_pages": int(math.ceil(len(self.__dataset) / page_size))
        }
