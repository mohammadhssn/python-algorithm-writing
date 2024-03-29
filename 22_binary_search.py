"""
    link: https://github.com/keon/algorithms/blob/master/algorithms/search/binary_search.py

    [1, 3, 5, 23, 34, 54, 55] , 54 => 5
"""


def binary_search(array, element):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        if val == element:
            return mid
        elif val < element:
            low = mid + 1
        else:
            high = mid - 1

    return None


print(binary_search([1, 3, 5, 23, 34, 54, 55], 54))
