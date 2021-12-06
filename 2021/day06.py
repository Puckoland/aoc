lines = open('input.txt', 'r').read().split(',')
fishes = list(map(lambda x: int(x), lines))

DAYS = 256


def part1():
    fishes1 = fishes[:]
    for _ in range(DAYS):
        for (i, fish) in enumerate(fishes1):
            if fish == 0:
                fishes1[i] = 6
                fishes1.append(9)
            else:
                fishes1[i] -= 1
    print(len(fishes1))


def part2():
    fishes2 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in fishes:
        fishes2[fish] += 1
    for _ in range(DAYS):
        new_born = 0
        for i in fishes2:
            if i == 0:
                new_born = fishes2[i]
                fishes2[i] = 0
            else:
                fishes2[i - 1] += fishes2[i]
                fishes2[i] = 0
        fishes2[8] = new_born
        fishes2[6] += new_born
    count = 0
    for fish in fishes2.values():
        count += fish
    print(count)


# part1()
part2()
