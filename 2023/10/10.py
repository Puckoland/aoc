import sys
sys.setrecursionlimit(100000)


def load_input():
    parts = open('input.txt', 'r').readlines()
    parts = list(map(lambda x: x.strip(), parts))
    return parts


class Tile:
    def __init__(self, tile):
        self.tile = tile
        self.visited = False
        self.is_start = tile == 'S'
        self.neighbours = []
        self._set_neighbours()


    def _set_neighbours(self):
        tile = self.tile
        if tile == '.':
            return
        if tile == 'S':
            self.neighbours.extend([(0, 1), (0, -1), (1, 0), (-1, 0)])
        elif tile == '-':
            self.neighbours.extend([(0, 1), (0, -1)])
        elif tile == '|':
            self.neighbours.extend([(1, 0), (-1, 0)])
        elif tile == 'L':
            self.neighbours.extend([(0, 1), (-1, 0)])
        elif tile == 'J':
            self.neighbours.extend([(0, -1), (-1, 0)])
        elif tile == '7':
            self.neighbours.extend([(0, -1), (1, 0)])
        elif tile == 'F':
            self.neighbours.extend([(0, 1), (1, 0)])

    def __repr__(self):
        return f'{self.tile}'


def create_maze(inp):
    maze = []
    for line in inp:
        lin = []
        for tile in line:
            lin.append(Tile(tile))
        maze.append(lin)
    return maze


def dfs(maze, coor, zanorenie=0):
    tile = maze[coor[0]][coor[1]]
    tile.visited = True
    for neighbour in tile.neighbours:
        neighbour_tile = maze[coor[0] + neighbour[0]][coor[1] + neighbour[1]]
        if neighbour_tile.is_start and zanorenie > 3:
            return 1
        if not neighbour_tile.visited:
            return 1 + dfs(maze, (coor[0] + neighbour[0], coor[1] + neighbour[1]), zanorenie + 1)
    return 0


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


def transform_maze(maze, coor, zanorenie=0):
    tile = maze[coor[0]][coor[1]]
    tile.visited = True
    tile.tile = '#'
    for neighbour in tile.neighbours:
        neighbour_tile = maze[coor[0] + neighbour[0]][coor[1] + neighbour[1]]
        if neighbour_tile.is_start and zanorenie > 3:
            return
        if not neighbour_tile.visited:
            transform_maze(maze, (coor[0] + neighbour[0], coor[1] + neighbour[1]), zanorenie + 1)


def fill_outside(maze):
    queue = (
            [(0, j) for j in range(len(maze[0]))]
            + [(len(maze) - 1, j) for j in range(len(maze[0]))]
            + [(i, 0) for i in range(len(maze))]
            + [(i, len(maze[0]) - 1) for i in range(len(maze))]
    )
    while queue:
        coor = queue.pop(0)
        tile = maze[coor[0]][coor[1]]
        if tile.tile == '#':
            continue
        tile.visited = True
        tile.tile = 'O'
        for neighbour in get_neigh_coors(coor[0], coor[1], len(maze), len(maze[0])):
            neighbour_tile = maze[neighbour[0]][neighbour[1]]
            if not neighbour_tile.visited:
                neighbour_tile.visited = True
                queue.append((neighbour[0], neighbour[1]))


def update_start_neighbours(maze, i, j):
    tile = maze[i][j]
    new_neighbours = []
    for neigh in tile.neighbours:
        neighbour_tile = maze[i + neigh[0]][j + neigh[1]]
        if neigh[0] == -1 and (neighbour_tile.tile == '|' or neighbour_tile.tile == '7' or neighbour_tile.tile == 'F'):
            new_neighbours.append(neigh)
        if neigh[0] == 1 and (neighbour_tile.tile == '|' or neighbour_tile.tile == 'L' or neighbour_tile.tile == 'J'):
            new_neighbours.append(neigh)
        if neigh[1] == -1 and (neighbour_tile.tile == '-' or neighbour_tile.tile == 'F' or neighbour_tile.tile == 'L'):
            new_neighbours.append(neigh)
        if neigh[1] == 1 and (neighbour_tile.tile == '-' or neighbour_tile.tile == '7' or neighbour_tile.tile == 'J'):
            new_neighbours.append(neigh)
    tile.neighbours = new_neighbours


def part_1(inp):
    maze = create_maze(inp)
    for i, line in enumerate(maze):
        for j, tile in enumerate(line):
            if tile.is_start:
                start_coor = (i, j)
                update_start_neighbours(maze, i, j)
                return dfs(maze, start_coor) // 2
    return -1


def part_2(inp):
    maze = create_maze(inp)
    for i, line in enumerate(maze):
        for j, tile in enumerate(line):
            if tile.is_start:
                start_coor = (i, j)
                update_start_neighbours(maze, i, j)
                transform_maze(maze, start_coor)
    fill_outside(maze)
    res = 0
    for line in maze:
        print(line)
        for tile in line:
            if tile.tile != 'O' and tile.tile != '#':
                res += 1
    return res


# print('Part 1: ', part_1(load_input()))
print('Part 2: ', part_2(load_input()))
# assert part_1(load_input()) == 1757008019
# assert part_2(load_input()) == 995
