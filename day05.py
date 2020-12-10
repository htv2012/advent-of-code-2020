#!/usr/bin/env python
import itertools


def select(lower, upper, selector):
    mid = (lower + upper) // 2
    if selector == "F" or selector == "L":
        return lower, mid
    elif selector == "B" or selector == "R":
        return mid + 1, upper
    raise ValueError(f"Invalid selector: {selector}")


def select_in_range(lower, upper, selectors):
    for selector in selectors:
        print(f"({lower}, {upper}) + {selector} => ", end="")
        lower, upper = select(lower, upper, selector)
        print((lower, upper))
    return lower


def seat_id(code):
    row = select_in_range(0, 127, code[:7])
    column = select_in_range(0, 7, code[-3:])
    return row * 8 + column


def main():
    pass


if __name__ == '__main__':
    main()
    with open("day05.txt") as stream:
        codes = stream.read().split()
    seat_ids = set(seat_id(code) for code in codes)
    max_seat_id = max(seat_ids)
    print(f"Max Seat ID: {max_seat_id}")

    # Part 2
    all_seats_ids = set(range(128*8))
    missing = all_seats_ids - seat_ids
    missing = sorted(missing)
    print(f"Missing: {missing}")
    a, b, c = itertools.tee(missing, 3)
    next(b)
    next(c); next(c)
    for lower, mid, upper in zip(a, b, c):
        if upper - mid > 1 and mid - lower > 1:
            print(lower, mid, upper)
