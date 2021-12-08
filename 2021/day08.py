lines = open('input.txt').read().splitlines()
entries = list(map(lambda line: list(map(lambda x: x.split(), line.split('|'))), lines))

KNOWN_LENGTHS = [2, 3, 4, 7]


def part1():
    count = 0
    for entry in entries:
        for out in entry[1]:
            if len(out) in KNOWN_LENGTHS:
                count += 1
    print(count)


def part2():
    pass


part1()
part2()
