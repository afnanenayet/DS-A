# quicksort.py
# Afnan Enayet
# A python implementation of quicksort


def quicksort(arr):
    """ sorts a subscriptable container containing elements that can be 
    compared
    :type arr: any subscriptable container
    :returns: a sorted array
    """
    # If the array only has 0 or 1 elements then return the array
    if arr is None or len(arr) < 2:
        return arr
