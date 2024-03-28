#!/usr/bin/env python3
"""Pagination helper func.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Fetches the index range based on a given page number and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
