def load_input():
    lines = open('input.txt', 'r').readlines()
    return list(map(lambda x: x.strip(), lines))


def build_schematic(lines):
    schematic = []
    for i, line in enumerate(lines):
        line_chars = []
        for ch in line:
            line_chars.append(ch)
        schematic.append(line_chars)
    return schematic


def get_neigh_coors(i, j, len_i, len_j):
    res = []
    if i > 0:
        res.append((i - 1, j))
        if j > 0:
            res.append((i - 1, j - 1))
        if j < len_j - 1:
            res.append((i - 1, j + 1))
    if i < len_i - 1:
        res.append((i + 1, j))
        if j > 0:
            res.append((i + 1, j - 1))
        if j < len_j - 1:
            res.append((i + 1, j + 1))
    if j > 0:
        res.append((i, j - 1))
    if j < len_j - 1:
        res.append((i, j + 1))
    return res


def to_num(line, left):
    digits = []
    for i in range(left, len(line)):
        if line[i].isnumeric():
            digits.append(int(line[i]))
        else:
            break
    return int(''.join(map(str, digits)))


def neighbour_nums(schematic, i, j):
    coors = get_neigh_coors(i, j, len(schematic), len(schematic[i]))
    numeric_neighbours = filter(lambda x: schematic[x[0]][x[1]].isnumeric(), coors)
    res = []
    for f in numeric_neighbours:
        num_start = f[1]
        while num_start > 0 and schematic[f[0]][num_start - 1].isnumeric():
            num_start -= 1
        res.append((f[0], num_start))
    res = list(set(res))
    return map(lambda x: to_num(schematic[x[0]], x[1]), res)


def part_1(lines):
    schematic = build_schematic(lines)
    numbers = []
    for i, line in enumerate(schematic):
        for j, ch in enumerate(line):
            if not ch.isnumeric() and ch != '.':
                numbers.extend(neighbour_nums(schematic, i, j))
    return sum(numbers)


def part_2(lines):
    schematic = build_schematic(lines)
    numbers = []
    for i, line in enumerate(schematic):
        for j, ch in enumerate(line):
            if ch == '*':
                neigh = list(neighbour_nums(schematic, i, j))
                if len(neigh) == 2:
                    numbers.append(neigh[0] * neigh[1])
    return sum(numbers)


assert part_1(load_input()) == 557705
assert part_2(load_input()) == 84266818
