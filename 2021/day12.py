lines = open('input.txt').read().splitlines()
edges = list(map(lambda x: x.split('-'), lines))


class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbours = []
        self.visited = False
        self.visited_double = False
        self.small = key.islower()

    def add_neighbor(self, nbr):
        self.neighbours.append(nbr)

    def __str__(self):
        return str(self.id) + " " + str(self.visited)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def add_edge(self, f, t):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t])
        self.vertices[t].add_neighbor(self.vertices[f])

    def __str__(self):
        return str([str(ver) for ver in self.vertices.values()])


def dfs(vertex):
    paths = []
    if vertex.visited:
        return []
    if vertex.small:
        vertex.visited = True
    if vertex.id == 'end':
        vertex.visited = False
        return [['end']]
    for neighbour in vertex.neighbours:
        for p in dfs(neighbour):
            p.append(vertex.id)
            paths.append(p)
    vertex.visited = False
    return paths


def dfs2(vertex, double_used):
    paths = []
    if vertex.visited:
        if double_used or vertex.id == 'start':
            return []
        double_used = True
        vertex.visited_double = True
    if vertex.small:
        vertex.visited = True
    if vertex.id == 'end':
        vertex.visited = False
        return [['end']]
    for neighbour in vertex.neighbours:
        for p in dfs2(neighbour, double_used):
            p.append(vertex.id)
            paths.append(p)
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
    paths = dfs(graph.vertices['start'])
    print(len(paths))


def part2():
    print(len(dfs2(create_graph().vertices['start'], False)))


part1()
part2()
