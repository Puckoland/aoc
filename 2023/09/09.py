def load_input():
    parts = open('input.txt', 'r').readlines()
    parts = list(map(lambda x: x.strip(), parts))
    parts = list(map(lambda x: x.split(), parts))
    parts = list(map(lambda x: list(map(lambda y: int(y), x)), parts))
    return parts


def differences(sequence):
    return [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]


def whats_next(sequence):
    if all(x == 0 for x in sequence):
        return 0
    diffs = differences(sequence)
    return sequence[-1] + whats_next(diffs)


def whats_before(sequence):
    if all(x == 0 for x in sequence):
        return 0
    diffs = differences(sequence)
    return sequence[0] - whats_before(diffs)


def part_1(sequences):
    res = 0
    for sequence in sequences:
        res += whats_next(sequence)
    return res


def part_2(sequences):
    res = 0
    for sequence in sequences:
        res += whats_before(sequence)
    return res


assert part_1(load_input()) == 1757008019
assert part_2(load_input()) == 995
