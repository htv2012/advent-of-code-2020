#!/usr/bin/env python
"""
https://adventofcode.com/2020/day/10
"""
import collections
import itertools

import logger


def gen(seen, li, dest):
    logger.debug(f"gen({seen}, {li})")
    last = seen[-1]
    if last == dest:
        yield seen
    for e in li:
        if 1 <= (e - last) <= 3:
            yield from gen(seen + [e], li, dest)

t = [int(x) for x in """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split()]
t.extend([0, 22])
t.sort()
print(f"t: {t}")

count = 0
for li in gen([0], t, 22):
    count += 1
    print(f"{count}: {li}")

if __name__ == '__main__':
    with open("day10.txt") as stream:
        numbers = [int(line.strip()) for line in stream]

    # print("Input:        ", numbers)
    numbers.sort()
    # print("Sorted input: ", numbers)
    numbers.insert(0, 0)
    numbers.append(numbers[-1] + 3)
    # print("Added ends:   ", numbers)

    # Find the diffs
    left_iter, right_iter = itertools.tee(numbers)
    next(right_iter)
    diffs = [right_e - left_e for right_e, left_e in zip(right_iter, left_iter)]
    # print("Diffs:        ", diffs)

    counter = collections.Counter(diffs)
    # print("Counter:      ", counter)
    answer1 = counter[1] * counter[3]
    print("Answer1:      ", answer1)

