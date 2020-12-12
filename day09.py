#!/usr/bin/env python
"""
https://adventofcode.com/2020/day/9
"""
from collections import deque
from itertools import combinations


def valid(buffer, target):
    """
    Can any 2 number in the buffer adds up to target?

    >>> valid([35, 20, 15, 25, 47], 40)
    True

    >>> valid([35, 20, 15, 25, 47], 41)
    False

    >>> valid([35, 20, 15, 25, 47], 35)
    True
    """
    return any(sum(t) ==  target  for t in combinations(buffer, 2))


def sumblock(sequence, right_index, total):
    """
    Finds the contigous block whose sum adds up to total, starting at index i
    and works backward (to the left)

    >>> sumblock([1, 2, 3, 4, 5], right_index=4, total=5)
    [4]

    >>> sumblock([1, 2, 3, 4, 5], right_index=3, total=7)
    [2, 3]

    >>> sumblock([1, 2, 3, 4, 5], right_index=3, total=9)
    [1, 2, 3]
    """
    if sequence[right_index] == total:
        return [right_index]

    sub_total = sequence[right_index]
    for left_index in range(right_index - 1, -1, -1):
        sub_total += sequence[left_index]
        if sub_total == total:
            return list(range(left_index, right_index + 1))
        elif sub_total > total:
            return sumblock(sequence, right_index - 1, total)

    return []





if __name__ == '__main__':
    with open("day09.txt") as stream:
        numbers = deque(int(line.strip()) for line in stream)
        original = [n for n in numbers]


    # Build up the preamble buffer
    preamble = 25
    buffer = deque(maxlen=preamble)
    for _ in range(preamble):
        n = numbers.popleft()
        buffer.append(n)

    while numbers:
        number = numbers.popleft()
        if not valid(buffer, number):
            # print(f"Buffer: {buffer}")
            print(f"Number: {number}")
            break
        buffer.append(number)

    # Part 2
    right_index = original.index(number) - 1
    indices = sumblock(original, right_index, number)
    block = [original[i] for i in indices]

    print(f"Contiguous block whose sum is {number}:")
    for i, e in zip(indices, block):
        print(f"[{i}] {e}")
    print("Sum:   ", sum(block))
    print("Number:", number)

    min_value = min(block)
    max_value = max(block)
    print("Min:   ", min_value)
    print("max:   ", max_value)
    print("Min + Max =", min_value + max_value)
