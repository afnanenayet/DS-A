""" Solution for the following programming problem:

Suppose you have a number that's represented as a linked list, as follows:

number: 54321, linked list: 1 -> 2 -> 3 -> 4 -> 5

The linked list contains each digit as a node, and is reversed from the actual
number.

Given two inputs, which are linked lists with the format described above,
add the two numbers together, and return the answer using the linked list
format that was described.

---

Potential solution:

Originally, I thought about converting each input to an actual integer, and
adding the numbers together, then converting the numbers back to a linked
list. This would give us an $\Theta(m + n)$ case runtime. We can do one better,
and actually do the addition on the fly with each digit, without converting
the inputs to numbers and back.

Instead, we can add each digit individually from each input, and incrementally
add the results of that addition to the output, as if we were doing the addition
by hand. We would also need to keep track of the number that's carried over.
Also consider what happens when there are mismatches in length between the two
numbers.

In a more concrete exmaple of what I'm proposing, suppose we have two inputs:

A: 52 (2 -> 5)
B: 45 (5 -> 4)

First, we will  add (2 + 5), making our running result 7. Then we will add
(5 + 4), making our running result 7 -> 9. This correspond to 97, and 52 + 45
= 97.
"""

# we can configure what base to do our math in
base = 10

class Node(object):
    """ A simple node for a singly linked list. It has a value and a `next`
    node.
    """

    def __init__(self, val, next_node=None):
        self.value = val
        self.next = next_node


def add_ll(A: Node, B: Node) -> Node:
    """ Add two numbers together that are defined as linked lists.
    These lists will both be assumed to represent valid numbers.

    :param A: the head node of a linked list
    :param B: the head node of a linked list
    :return: the head of the resultant node
    """
    carry = 0  # the value to carry over for each digit
    ret = None
    head = ret

    # define iterators to walk through each linked list
    it_A = A
    it_B = B

    # walk through lists A and B simultaneously while they both have digits
    # we can add together
    while it_A is not None and it_B is not None:
        next_digit = carry + it_A.value + it_B.value
        carry = next_digit // base
        digit = next_digit % base

        # initialize the linked list if it hasn't been initialized, otherwise
        # append to it
        if ret:
            ret.next = Node(digit)
            ret = ret.next
        else:
            head = Node(digit)
            ret = head

        # iterate to next
        it_A = it_A.next
        it_B = it_B.next

    # only one of these loops will ever run, because the exit condition for
    # the previous loop mandates that either it_A or it_B is `None`. If either
    # of them are `None`, then their loop will not execute.
    while it_A is not None:
        n = it_A.value + carry
        ret.next = n % base
        ret = ret.next
        carry = n // base
        it_A = it_A.next

    while it_B is not None:
        n = it_B.value + carry
        ret.next = n % base
        ret = ret.next
        carry = n // base
        it_B = it_B.next

    if carry != 0:
        ret.next = Node(carry)

    return head


def ll_to_num(ll: Node) -> int:
    """ Converts a linked list to a number, as according to the specification
    in the docstring. This is a convenience function for testing. It is
    assumed that the linked list will represent a valid number.

    :param ll: the head of a linked list representing a number.
    :return: the normal integer form of the linked list
    """
    it: Node = ll
    assert(type(it) == Node)
    num = 0
    exp = 0

    while it:
        val: int = it.value
        num += val * (base ** exp)
        it = it.next
        exp += 1
    return num


def num_to_ll(num: int) -> Node:
    """ Converts a number to a linked list in the format described in the
    docstring. This is a convenience function for testing.

    :param num: the input
    :return: the linked list format of the integer
    """
    ll = None
    head = ll

    while num > 0:
        next_val = num % base
        num = num // base

        if ll:
            ll.next = Node(next_val)
            ll = ll.next
        else:
            ll = Node(next_val)
            head = ll
    return head


def main():
    """ Wrapper for main function.
    """
    import random
    import sys

    # testing that linked list to number conversions are accurate
    for _ in range(10000):
        r = random.randint(0, sys.maxsize)
        ll = num_to_ll(r)
        num = ll_to_num(ll)
        assert(num == r)

    for _ in range(10000):
        r = random.randint(0, sys.maxsize)
        ll = num_to_ll(r)
        added = add_ll(ll, None)
        num = ll_to_num(added)
        assert(r == num)

    # testing the actual addition function
    for _ in range(10000):
        a = random.randint(0, sys.maxsize)
        b = random.randint(0, sys.maxsize)

        ll_a = num_to_ll(a)
        ll_b = num_to_ll(b)

        ll_res = add_ll(ll_a, ll_b)
        # res = ll_to_num(ll_res)

        # assert(res == (a + b))


if __name__ == "__main__":
    main()
