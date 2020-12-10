#!/usr/bin/env python3
"""
A Python skeleton script
"""
import functools


def count_answer(group):
    group = group.replace("\n", "")
    return len(set(group))


def count_answer2(group):
    answers = [set(x) for x in group.split()]
    common = functools.reduce(set.intersection, answers)
    return len(common)


def main():
    # Read the file
    with open("day06.txt") as stream:
        groups = [
            group
            for group in stream.read().split("\n\n")
        ]

    # Debugging
    for group in groups:
        print(f"\n{group} => {count_answer2(group)}")

    total = sum(count_answer(group) for group in groups)
    print(f"Sum of counts: {total}")

    total2 = sum(count_answer2(group) for group in groups)
    print(f"Sum of counts 2: {total2}")




if __name__ == '__main__':
    main()
