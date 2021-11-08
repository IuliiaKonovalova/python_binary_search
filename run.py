"""
Binary search implementation
Comparing with naive search
"""

def naive_search(list_to_search, target):
    for i in range(len(list_to_search)):
        if list_to_search[i] == target:
            return i
    return -1

def binary_search(list_to_search, target, low=None, high=None):
    
    if low is None:
        low = 0
    if high is None:
        high = len(list_to_search) - 1
    
    mid_point = (len(list_to_search)) // 2

    if list_to_search == target:
        return mid_point
    elif target < list_to_search[mid_point]:
        return binary_search(list_to_search, target, low, mid_point-1)
    else:
        return binary_search(list_to_search, target, mid_point+1, high)
