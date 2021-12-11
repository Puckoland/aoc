lines = open('input.txt').read().splitlines()

SIZE_Y = len(lines)
SIZE_X = len(lines[0])

STEPS = 100


def get_adjacent(y, x):
    adjacent = []
    if y > 0:
        adjacent.append((y - 1, x))
        if x > 0:
            adjacent.append((y - 1, x - 1))
        if x < SIZE_X - 1:
            adjacent.append((y - 1, x + 1))
    if x > 0:
        adjacent.append((y, x - 1))
    if y < SIZE_Y - 1:
        adjacent.append((y + 1, x))
        if x > 0:
            adjacent.append((y + 1, x - 1))
        if x < SIZE_X - 1:
            adjacent.append((y + 1, x + 1))
    if x < SIZE_X - 1:
        adjacent.append((y, x + 1))
    return adjacent


def light(nums, coor, lighted, count):
    y, x = coor
    if (y, x) in lighted:
        return count
    if nums[y][x] < 9:
        nums[y][x] += 1
        return count
    nums[y][x] = 0
    lighted.append((y, x))
    for adj in get_adjacent(y, x):
        count = light(nums, adj, lighted, count)
    return count + 1


def step(nums, count):
    lighted = []
    for y in range(len(nums)):
        for x in range(len(nums)):
            count = light(nums, (y, x), lighted, count)
    return count


def part1():
    nums = list(map(lambda x: [int(c) for c in x], lines))
    count = 0
    for _ in range(STEPS):
        count = step(nums, count)
    print(count)


def part2():
    nums = list(map(lambda x: [int(c) for c in x], lines))
    count = 0
    steps = 0
    while not False:
        steps += 1
        step(nums, count)
        if sum(list(map(lambda x: sum(x), nums))) == 0:
            print(steps)
            return


part1()
part2()
