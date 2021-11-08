"""
Binary search implementation
Comparing with naive search
"""

def naive_search(list_to_search, target):
    for i in range(len(list_to_search)):
        if list_to_search[i] == target:
            return i
    return -1

