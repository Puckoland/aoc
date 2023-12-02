import re
import math

lines = open('input.txt', 'r').readlines()


def parse_move_parts(move):
    num, color = move.split(" ")
    return int(num), color


def parse_moves(line):
    start_index = line.index(":") + 2
    moves_string = line[start_index:-1]
    moves = re.split("; |, ", moves_string)
    return map(lambda x: parse_move_parts(x), moves)


def part_1():
    available = {"red": 12, "green": 13, "blue": 14}
    possibles = []
    for i, line in enumerate(lines):
        for num, color in parse_moves(line):
            if num > available[color]:
                break
        else:
            possibles.append(i + 1)
    return sum(possibles)


def part_2():
    powers = []
    for i, line in enumerate(lines):
        needed = {}
        for num, color in parse_moves(line):
            needed[color] = max(needed.get(color, 0), num)
        powers.append(math.prod(needed.values()))
    return sum(powers)


assert part_1() == 2447
assert part_2() == 56322
