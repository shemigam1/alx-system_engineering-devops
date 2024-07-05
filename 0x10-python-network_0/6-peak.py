#!/usr/bin/python3
"""
Finds the peak in a list of unsorted ints
"""


def find_peak(list_of_integers):
    """
    args: list_of_integers(int)
    return: peak(int)
    """
    size = len(list_of_integers)
    mid = size
    middle = size // 2
    loi = list_of_integers

    if size == 0:
        return None

    while True:
        mid = mid // 2
        if (middle < size - 1 and
                loi[middle] < loi[middle + 1]):
            if mid // 2 == 0:
                mid = 2
            middle = middle + mid // 2
        elif mid > 0 and loi[middle] < loi[middle + 1]:
            if mid // 2 == 0:
                mid = 2
            middle = middle - mid // 2
        else:
            return loi[middle]
