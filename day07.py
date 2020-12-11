#!/usr/bin/env python
"""
https://adventofcode.com/2020/day/7
"""
import re


def parse(line):
    line = line.strip().rstrip(".")
    container, rest = line.split(" bags contain ")

    # Now rest looks something like:
    # '4 drab lavender bags, 1 clear orange bag, 2 striped black bags'
    if "no other bags" in rest:
        rest = []
    else:
        pattern = re.compile(r"(\d+) (.*) bags?")
        rest = [pattern.match(x).groups() for x in rest.split(", ")]
        rest = [(int(count), color) for count, color in rest]

    return container, rest


def traverse(bags, source):
    for count, node in bags.get(source, []):
        yield count, node
        if node in bags:
            for count2, node2 in traverse(bags, node):
                yield count * count2, node2


def count_containers(bags, bag, expected_count):
    containers = set(
        node for count, node in traverse(bags, bag)
        if count >= expected_count
    )
    return len(containers)


def main():
    # Parse the data file
    inside_bags = {}
    containers = {}
    with open("day07.txt") as stream:
        for line in stream:
            container, contents = parse(line)
            for count, bag in contents:
                inside_bags.setdefault(bag, []).append((count, container))
                containers.setdefault(container, []).append((count, bag))


    answer1 = count_containers(inside_bags, "shiny gold", 1)
    print(f"Answer 1: {answer1}")

    answer2 = sum(c for c, _ in traverse(containers, "shiny gold"))
    print(f"Answer 2: {answer2}")


if __name__ == "__main__":
    main()
