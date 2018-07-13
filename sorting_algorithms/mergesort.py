# mergesort.py
# Python3 implementation of mergesort

import math


def mergesort(arr):
    """ Implementation of mergesort in Python 3
    Uses a recursive approach to merge and sort subarrays until whole array 
    is sorted
    :arr type: list
    :rtype: list
    """
    # base cases
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return [arr[0], arr[1]]

    k = math.ceil(len(arr) / 2)
    arr1 = arr[:k]
    arr2 = arr[k:]

    sorted1 = mergesort(arr1)
    sorted2 = mergesort(arr2)
    return merge_helper(sorted1, sorted2)


def merge_helper(arr1, arr2):
    """ Merges two arrays in increasing order
    :type arr1: list
    :type arr2: list
    :rtype: list
    """

    i = 0  # index for arr1
    j = 0  # index for arr2
    ret = list()

    # iterate through both arrays, creating a new list that takes new elements
    # in increasing order
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ret.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            ret.append(arr2[j])
            j += 1
        else:
            # case where both elements are equal, order doesn't matter
            ret.append(arr1[i])
            ret.append(arr2[j])
            j += 1
            i += 1

    # append remainders
    while i < len(arr1):
        ret.append(arr1[i])
        i += 1

    while j < len(arr2):
        ret.append(arr2[j])
        j += 1

    return ret


# test
test1 = [0, 4, 3, 2, 1]
res1 = mergesort(test1)
print(res1)
