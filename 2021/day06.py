lines = open('input.txt', 'r').read().split(',')
fishes = list(map(lambda x: int(x), lines))

DAYS = 80


def part1():
    for _ in range(DAYS):
        for (i, fish) in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                fishes.append(9)
            else:
                fishes[i] -= 1
    print(len(fishes))


def part2():
    print()


part1()
part2()
