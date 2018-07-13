# countsort.py
# implementation of count sort in Python 3
# Afnan Enayet

import random


def count_sort(arr, max_element):
    """ count sort, an O(n) sorting algorithm that just records the frequency
    of each element in an array
    :type arr: list
    :type max_element: int
    :rtype: list
    """
    # initializing variables
    freq = [0 for _ in range(max_element + 1)]
    ret = list()

    # count frequencies of each element
    for element in arr:
        freq[element] += 1

    # create the return array from a list
    for i in range(len(freq)):
        # append the element to the return array as many times as it appears
        # in the original array
        for _ in range(freq[i]):
            ret.append(i)
    return ret


# test by generating random lists and making sure they are equal to python's
# sorted list (an algorithm we know to be correct)
success = True

# test with 100 different arrays
for _ in range(100):
    random_list = random.sample(range(100), 10)
    test1 = count_sort(random_list, max(random_list))

    if not (test1 == sorted(random_list)):
        success = False

if success:
    print("Success")
else:
    print("Error, test failed")
