class Edge:
    def __init__(self, dest, capa):
        self.dest = dest
        self.capa = capa
        self.rmng = capa


class Node:
    def __init__(self, name, level=0, edges=None):
        self.name = name
        self.level = level
        if edges is None:
            self.edges = []

    def add_edge(self, dest, weight):
        self.edges.append(Edge(dest, weight))

    def get_children(self):
        res = []
        for edge in self.edges:
            res.append(edge.dest)
        return res

    def __str__(self):
        res = str(self.name) + " ({})".format(str(self.level))
        for edge in self.edges:
            res = res + " --> {} ({})".format(str(edge.dest), str(edge.rmng))
        return res


class Graph:
    nodes = []
    flow = []
    perma_dead = []
    levels = []

    def __init__(self, entrances, exits, matrix):
        self.entrances = entrances
        self.exits = exits
        self.matrix = matrix
        for i in range(0, len(self.matrix)):
            self.nodes.append(Node(i))

    def create(self):
        for i in range(0, len(self.matrix)):
            if self.nodes[i].name in self.exits:
                continue
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    self.nodes[i].add_edge(j, self.matrix[i][j])

    def bfs(self):
        queue = self.entrances[:]
        seen = self.entrances[:]
        level = 0
        self.levels = [-1] * len(self.matrix)
        for entrance in self.entrances:
            self.nodes[entrance].level = level
            self.levels[entrance] = level
        while len(queue) > 0:
            to_remove = []
            i = queue.pop(0)
            level = self.nodes[i].level + 1
            for edge in self.nodes[i].edges:
                if edge.dest in self.perma_dead:
                    to_remove.append(edge)
                elif edge.rmng > 0:
                    if edge.dest not in seen:
                        self.nodes[edge.dest].level = self.levels[edge.dest] = level
                        queue.append(edge.dest)
                        seen.append(edge.dest)
                else:
                    to_remove.append(edge)
            for edge in to_remove:
                self.nodes[i].edges.remove(edge)
        if self.is_finished():
            return False
        return True

    def is_finished(self):
        for ex in self.exits:
            if self.levels[ex] != -1:
                return False
        return True

    def choose_next_node(self, candidates, dead_ends):
        for i in candidates:
            previous_level = self.nodes[i].level
            for edge in self.nodes[i].edges:
                if (edge.rmng > 0) \
                        and (previous_level < self.nodes[edge.dest].level)\
                        and (edge.dest not in dead_ends):
                    return i, edge, edge.rmng
        return None, None, None

    def dfs(self):
        paths, capas, edges = [], [], []
        dead_ends = self.perma_dead[:]
        entr = self.entrances[:]
        current_node, edge, capa = self.choose_next_node(entr, dead_ends)
        next_node = None
        if edge is not None:
            next_node = edge.dest
            edges.append(edge)
            paths.append(current_node)
            if next_node in self.exits:
                paths.append(next_node)
                capas.append(capa)
        else:
            return

        while next_node not in self.exits and len(paths) > 0:
            if next_node != paths[-1]:
                paths.append(next_node)
                capas.append(capa)
            current_node, edge, capa = self.choose_next_node([next_node], dead_ends)
            if edge is not None:
                next_node = edge.dest
                edges.append(edge)
                if next_node in self.exits:
                    paths.append(next_node)
                    capas.append(capa)
            else:
                if len(paths) > 1:
                    dead_ends.append(paths[-1])
                    paths, edges, capas = paths[:-1], edges[:-1], capas[:-1]
                    next_node = paths[-1]
                else:
                    entr.remove(paths[0])
                    paths, capas = [], []
                    current_node, edge, capa = self.choose_next_node(entr, dead_ends)
                    next_node = None
                    if edge is not None:
                        next_node = edge.dest
                        edges.append(edge)
                        paths.append(current_node)
                        if next_node in self.exits:
                            paths.append(next_node)
                            capas.append(capa)
                    else:
                        return
        if len(paths) < 1:
            return False
        capa = min(capas)
        self.flow.append(capa)
        i = 0
        for edge in edges:
            edge.rmng -= capa
            if not edge.rmng:
                self.nodes[paths[i]].edges.remove(edge)
                if len(self.nodes[paths[i]].edges) < 1:
                    self.perma_dead.append(self.nodes[paths[i]].name)
            i += 1
        return False


def solution(entrances, exits, matrix):
    graph = Graph(entrances,  exits, matrix)
    graph.create()
    while graph.bfs():
        graph.dfs()
    return sum(graph.flow)

entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]
print(solution(entrances, exits, path))
