#!/usr/bin/env python
"""
https://adventofcode.com/2020/day/8
"""
def parse_line(line):
    op, count = line.split()
    count = int(count)
    return op, count


def run(code):
    print("-" * 80)
    visited = set()
    acc  = 0
    line = 0

    while True:
        if line in visited:
            print(f"Accumulator contains {acc}")
            return True, acc

        visited.add(line)
        try:
            instruction, count = code[line]
        except IndexError:
            return False, acc

        print(f"{line:>3} {instruction} {count}")

        if instruction == "nop":
            line += 1
        elif instruction == "acc":
            acc += count
            print(f"    A={acc}")
            line += 1
        elif instruction == "jmp":
            line += count


def swap_instruction(instruction):
    if instruction == "jmp":
        return "nop"
    elif instruction == "nop":
        return "jmp"


if __name__ == '__main__':
    with open("day08.txt") as stream:
        code = [parse_line(line) for line in stream]

    iloop, acc = run(code)
    print(f"Infinite loop? {iloop}, acc={acc}")

    for line_number, (instruction, count) in enumerate(code):
        if instruction == "nop" or instruction == "jmp":
            new_instruction = swap_instruction(instruction)
            code[line_number] = (new_instruction, count)
            iloop, acc = run(code)
            if not iloop:
                print(
                    f"Fixed by changing line {line_number}"
                    f" from '{instruction} {count}'"
                    f" to  '{new_instruction} {count}'"
                )
                print(f"acc = {acc}")
                break
            code[line_number] = (instruction, count)
