lines = open('input.txt').read().splitlines()

SIZE_Y = len(lines)
SIZE_X = len(lines[0])

STEPS = 100


def get_adjacent(y, x):
    adjacent = []
    for dy in range(-1 if y > 0 else 0, 2 if y < SIZE_Y - 1 else 1):
        for dx in range(-1 if x > 0 else 0, 2 if x < SIZE_X - 1 else 1):
            if dx != 0 or dy != 0:
                adjacent.append((y + dy, x + dx))
    return adjacent


def add_one(nums, coor, lighted, count):
    y, x = coor
    if (y, x) in lighted:
        return count
    if nums[y][x] < 9:
        nums[y][x] += 1
        return count
    nums[y][x] = 0
    lighted.append((y, x))
    for adj in get_adjacent(y, x):
        count = add_one(nums, adj, lighted, count)
    return count + 1


def step(nums, count):
    lighted = []
    for y in range(len(nums)):
        for x in range(len(nums)):
            count = add_one(nums, (y, x), lighted, count)
    return count


def part1():
    nums = list(map(lambda x: [int(c) for c in x], lines))
    count = 0
    for _ in range(STEPS):
        count = step(nums, count)
    print(count)


def part2():
    nums = list(map(lambda x: [int(c) for c in x], lines))
    steps = 0
    while True:
        steps += 1
        count = step(nums, 0)
        if count == SIZE_Y * SIZE_X:
            print(steps)
            return


part1()
part2()
