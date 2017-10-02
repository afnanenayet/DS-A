# generate_subsets.py
# Afnan Enayet
# an algorithm to generate all subsets of a set
# note that this does not currently work likely because of an issue with 
# references, but it gets the general idea

def gen_subsets(arr):
    """ generates all subsets of a set of elements/list
    Works by backtracking: every element either is or
    isn't in a set. The recursive call stack essentially
    is a tree where every left branch is not including the
    element in the subset and every right branch is including
    that element in the subset
    :type arr: list
    :rtype: List[list]
    """
    subsets = [[]]
    curr_sub = []
    return subset_helper(arr, curr_sub, subsets, 0)


def subset_helper(arr, curr_sub, subsets, k):
    """ helper method for gen_subsets that includes a list of subsets to
    push to
    :type arr: list
    :type curr: list
    :type ret: list
    :type k: int
    :rtype: List[list]
    """

    # process subset
    if k == len(arr):
        print(curr_sub)
        return subsets.append(curr_sub)

    # Two cases: we either add the current element, or we don't
    # this creates a new "branch", and from there we call the 
    # function again
    minus_one = curr_sub

    if curr_sub is None:
        plus_one = [arr[k]]
        minus_one = []
    else:
        plus_one = curr_sub.append(arr[k])

    subset_helper(arr, minus_one, subsets, k + 1)
    subset_helper(arr, plus_one, subsets, k + 1)
    return subsets

# Test
test_arr = [1, 2]
print(gen_subsets(test_arr))

