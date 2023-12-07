from itertools import cycle
import math


def load_input():
    parts = open('input.txt', 'r').read().split("\n\n")
    instructions, mappings = parts
    instructions = instructions.replace("R", "1").replace("L", "0")
    ins = [int(x) for x in instructions]
    mappings = mappings.split("\n")
    res = {}
    for mapping in mappings:
        key, value = mapping.split(" = ")
        left, right = value.split(", ")
        left = left[1:]
        right = right[:-1]
        res[key] = (left, right)
    return ins, res


def part_1(inp):
    instructions, mappings = inp
    instructions = cycle(instructions)
    steps = 0
    start = "AAA"
    for instruction in instructions:
        if start == "ZZZ":
            break
        steps += 1
        start = mappings[start][instruction]
    return steps



def part_2(inp):
    instructions, mappings = inp
    starts = [key for key in mappings.keys() if key.endswith("A")]
    end_indexes = [0 for _ in starts]
    cycles = [0 for _ in starts]
    for step, instruction in enumerate(cycle(instructions)):
        if not any(x == 0 for x in cycles):
            break

        for i, start in enumerate(starts):
            starts[i] = mappings[start][instruction]
            if start.endswith("Z"):
                if end_indexes[i] == 0:
                    end_indexes[i] = step
                elif cycles[i] == 0:
                    cycles[i] = step - end_indexes[i]

    return math.lcm(*cycles)


assert part_1(load_input()) == 18727
assert part_2(load_input()) == 18024643846273
