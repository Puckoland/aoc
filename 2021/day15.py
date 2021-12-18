from queue import PriorityQueue

lines = open('input.txt').read().splitlines()
nums = list(map(lambda x: [int(c) for c in x], lines))

SIZE_Y = len(nums)
SIZE_X = len(nums[0])


def get_adjacent(coor):
    y, x = coor
    adjacent = []
    for dy in range(-1 if y > 0 else 0, 2 if y < SIZE_Y - 1 else 1):
        for dx in range(-1 if x > 0 else 0, 2 if x < SIZE_X - 1 else 1):
            if (dx != 0 or dy != 0) and (dx == 0 or dy == 0):
                adjacent.append((y + dy, x + dx))
    return adjacent


def dijkstra(queue):
    queue.put((0, (0, 0)))
    visited = [(0, 0)]
    while not queue.empty():
        val, coor = queue.get()
        if coor == (SIZE_Y - 1, SIZE_X - 1):
            return val
        for adj in get_adjacent(coor):
            adj_val = nums[adj[0]][adj[1]]
            if adj not in visited:
                queue.put((val + adj_val, adj))
                visited.append(adj)


def part1():
    queue = PriorityQueue()
    print(dijkstra(queue))


def part2():
    pass


part1()
part2()
