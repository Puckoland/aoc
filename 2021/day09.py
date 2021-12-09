lines = open('input.txt').read().splitlines()
nums = list(map(lambda x: [int(c) for c in x], lines))

SIZE_Y = len(lines)
SIZE_X = len(lines[0])


def get_adjacent(y, x):
    adjacent = []
    if y > 0:
        adjacent.append((y - 1, x, nums[y - 1][x]))
    if x > 0:
        adjacent.append((y, x - 1, nums[y][x - 1]))
    if y < SIZE_Y - 1:
        adjacent.append((y + 1, x, nums[y + 1][x]))
    if x < SIZE_X - 1:
        adjacent.append((y, x + 1, nums[y][x + 1]))
    return adjacent


def get_low_points():
    low_points = []
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            if nums[y][x] < min(map(lambda a: a[2], get_adjacent(y, x))):
                low_points.append((y, x, nums[y][x]))
    return low_points


def part1():
    low_points = list(map(lambda x: x[2], get_low_points()))
    print(sum(low_points) + len(low_points))


def bfs(to_do, basin):
    while len(to_do) != 0:
        y, x, point = to_do.pop(0)
        adj = get_adjacent(y, x)
        for y, x, a in adj:
            if a < 9 and (y, x, a) not in basin:
                to_do.append((y, x, a))
                basin.append((y, x, a))


def part2():
    basins_sizes = []
    for low in get_low_points():
        to_do = [low]
        basin = [low]
        bfs(to_do, basin)
        basin = list(map(lambda b: b[2], basin))
        basins_sizes.append(len(basin))
    basins_sizes.sort(reverse=True)
    product = 1
    for size in basins_sizes[:3]:
        product *= size
    print(product)


part1()
part2()
