"""
Binary search implementation
Comparing with naive search
"""

import random
import time


def naive_search(list_to_search, target):
    """
    Naive search function
    """
    for i in range(len(list_to_search)):
        if list_to_search[i] == target:
            return i
    return -1

def binary_search(list_to_search, target, low=None, high=None):
    """
    Binary search function
    """
    if low is None:
        low = 0
    if high is None:
        high = len(list_to_search) - 1

    if high < low:
        return -1
    
    mid_point = (low + high) // 2

    if list_to_search == target:
        return mid_point
    elif target < list_to_search[mid_point]:
        return binary_search(list_to_search, target, low, mid_point-1)
    else:
        return binary_search(list_to_search, target, mid_point+1, high)


if __name__ == '__main__':
    # list1 = [1, 3, 5, 6, 7, 9, 11, 13, 15, 20]
    # target1 = 9
    # print(naive_search(list1, target1))
    # print(binary_search(list1, target1))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f'Naive search {end - start/length} sec')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f'Binary search {end - start/length} sec')
