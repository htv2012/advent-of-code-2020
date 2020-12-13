#!/usr/bin/env python
"""
https://adventofcode.com/2020/day/10
"""
import collections
import itertools


if __name__ == '__main__':
    with open("day10.txt") as stream:
        numbers = [int(line.strip()) for line in stream]

    print("Input:        ", numbers)
    numbers.sort()
    print("Sorted input: ", numbers)
    numbers.insert(0, 0)
    numbers.append(numbers[-1] + 3)
    print("Added ends:   ", numbers)

    # Find the diffs
    left_iter, right_iter = itertools.tee(numbers)
    next(right_iter)
    diffs = [right_e - left_e for right_e, left_e in zip(right_iter, left_iter)]
    print("Diffs:        ", diffs)

    counter = collections.Counter(diffs)
    print("Counter:      ", counter)
    answer1 = counter[1] * counter[3]
    print("Answer1:      ", answer1)
