#!/usr/bin/env python
"""
Before you leave, the Elves in accounting just need you to fix your
expense report (your puzzle input); apparently, something isn't
quite adding up.

Specifically, they need you to find the two entries that sum to
2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the
correct answer is 514579.

Of course, your expense report is much larger. Find the two entries
that sum to 2020; what do you get if you multiply them together?
"""
import itertools
import functools
import operator


def main():
    """ Entry """
    with open('day01.txt') as stream:
        numbers = [int(x.strip()) for x in stream]

    # Part 1
    for number in numbers:
        other = 2020 - number
        if other in numbers:
            print(f"{number} x {other} = {number * other}")
            break

    # Part 2
    for triplet in itertools.combinations(numbers, 3):
        if sum(triplet) == 2020:
            print(' x '.join(str(x) for x in triplet), end=" = ")
            print(functools.reduce(operator.mul, triplet))
            break


if __name__ == '__main__':
    main()
