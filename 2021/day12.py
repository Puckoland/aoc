lines = open('input.txt').read().splitlines()
edges = list(map(lambda x: x.split('-'), lines))

START = "start"
END = "end"


class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbours = []
        self.visited = False
        self.visited_double = False
        self.small = key.islower()

    def add_neighbor(self, nbr):
        self.neighbours.append(nbr)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, f, t):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t])
        self.vertices[t].add_neighbor(self.vertices[f])


def dfs(vertex):
    paths = []
    if vertex.visited:
        return paths
    if vertex.small:
        vertex.visited = True
    if vertex.id == END:
        vertex.visited = False
        return [[END]]
    for neighbour in vertex.neighbours:
        for path in dfs(neighbour):
            path.append(vertex.id)
            paths.append(path)
    vertex.visited = False
    return paths


def dfs2(vertex, double_used):
    paths = []
    if vertex.visited:
        if double_used or vertex.id == START:
            return paths
        double_used = True
        vertex.visited_double = True
    if vertex.small:
        vertex.visited = True
    if vertex.id == END:
        vertex.visited = False
        return [[END]]
    for neighbour in vertex.neighbours:
        for path in dfs2(neighbour, double_used):
            path.append(vertex.id)
            paths.append(path)
    if vertex.visited_double:
        vertex.visited_double = False
    else:
        vertex.visited = False
    return paths


def create_graph():
    graph = Graph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    return graph


def part1():
    graph = create_graph()
    paths = dfs(graph.vertices[START])
    print(len(paths))


def part2():
    graph = create_graph()
    paths = dfs2(graph.vertices[START], False)
    print(len(paths))


part1()
part2()
