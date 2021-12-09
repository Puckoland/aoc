lines = open('input.txt').read().splitlines()
nums = list(map(lambda x: [int(c) for c in x], lines))

SIZE_Y = len(lines)
SIZE_X = len(lines[0])


def part1():
    low_points = []
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            adjacent = []
            if y > 0:
                adjacent.append(nums[y - 1][x])
            if x > 0:
                adjacent.append(nums[y][x - 1])
            if y < SIZE_Y - 1:
                adjacent.append(nums[y + 1][x])
            if x < SIZE_X - 1:
                adjacent.append(nums[y][x + 1])
            if nums[y][x] < min(adjacent):
                low_points.append(nums[y][x])
    print(sum(low_points) + len(low_points))


def part2():
    pass


part1()
part2()
