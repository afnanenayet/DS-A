"""
# Tower of Hanoi

This is the classic Tower of Hanoi problem. A lot of people are very
familiar with this one already, so I wouldn't expect to ever see this in
an interview. That being said, why not.

---

## The problem

The Tower of Hanoi is a puzzle game with three rods, and `n` disks. Each
disk is of a different size.  All the disks start off in a stack on the
first rod, ordered by size, from smallest to largest (so the bottom disk
is the largest).

The objective of this puzzle is to move every rod from the first rod to
the third rod, preserving the order of the disks.

There are a few constraints you are subject to:

- you can only move one disk at a time
- a move consists of taking the top disk of one stack and placing it on the
  top of another stack
- you cannot place a larger disk on top of a smaller disk

Your function must print out all of the moves required to win the game.

Example: for n = 3

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3


## The approach

This is a classically recursive problem. With any recursive problem, the first
thing you think of should be the subproblems -- how do you break the problem
down into subproblems and the base case.

In the towers of hanoi problem, we know that the base case is when we have
only one disk. We move the disk from wherever it is to the desired target
(in this case, the third rod).

Suppose the first rod is `starting_rod`, the middle rod is `aux_rod` (for
auxiliary rod), and the third rod is `dest_rod` for destination rod. Then,
for each subproblem `n`, we want to move `n-1` rods from the source
to `aux_rod`, and move the last disk to the end, then move all of the disks
from `aux_rod` to `dest_rod` (2 -> 3).

You can see how this is a recursive problem, since each answer builds off of
the solution for the `n - 1` problem.
"""


def hanoi_helper(n: int, source_rod, aux_rod, dest_rod):
    """ Given a number of disks, solves the tower of hanoi puzzle and prints
    out the steps required to win the game.

    :param n: the number of disks
    """
    # base case
    if n == 1:
        print(f"{source_rod} -> {dest_rod}")
        return

    # move rods from source to aux, using the destination as the "auxiliary"
    hanoi_helper(n - 1, source_rod, dest_rod, aux_rod)

    # move the last rod from the source to the dest
    print(f"{source_rod} -> {dest_rod}")

    # move all rods from aux to dest, using source as the "auxiliary"
    hanoi_helper(n - 1, aux_rod, source_rod, dest_rod)


def hanoi(n: int):
    """ A wrapper function to kick off the process, since we know source, aux
    and dest starting out.

    :param n: the number of disks to use for the problem
    """
    hanoi_helper(n, 1, 2, 3)


def main():
    """ Wrapper for main function
    """
    inputs = [
        3,
        4,
    ]

    for disks in inputs:
        print(f"\n\nTowers of Hanoi with {disks} disks\n---\n")
        hanoi(disks)


if __name__ == "__main__":
    main()
