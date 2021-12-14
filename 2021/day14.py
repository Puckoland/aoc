import math

lines = open('input.txt').read().splitlines()
start = [char for char in lines[0]]
insert = dict(map(lambda x: x.split(" -> "), lines[2:]))





def get_result(template):
    # counts = {}
    # for char in template:
    #     if counts.get(char):
    #         counts[char] += 1
    #     else:
    #         counts[char] = 1
    # return max(counts.values()) - min(counts.values())
    return template.count(max(template, key=template.count)) - template.count(min(template, key=template.count))


def do(steps):
    template = start.copy()
    for _ in range(steps):
        to_add = []
        for i in range(len(template) - 1):
            to_add.append(insert.get(template[i] + template[i + 1]))
        for i, add in enumerate(to_add):
            template.insert(2 * i + 1, add)
    print(get_result(template))


def part1():
    do(10)


def part2():
    do(40)


part1()
part2()
