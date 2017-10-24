import queue


def adjacency_list(vertex_c, edges, directed=False, simple=True):
    node_list = [[] for _ in range(vertex_c)]
    for u, v in edges:
        if u < vertex_c or v < vertex_c:
            if simple or v not in node_list[u]:
                node_list[u].append(v)
                if not directed:
                    node_list[v].append(u)
    return node_list


def adjacency_mat(vertex_c, edges, directed=False):
    mat = [[0 for _ in range(vertex_c)] for _ in range(vertex_c)]
    for u, v in edges:
        if u < vertex_c or v < vertex_c:
            mat[u][v] += 1
            if not directed:
                mat[v][u] += 1
    return mat


def input_graph():
    n = int(input('Enter the number of vertices: '))
    print('Enter the edges(u v):')
    edges = []
    while True:
        ip = input()
        try:
            u, v = tuple(ip.split())
            edges.append((int(u), int(v)))
        except ValueError:
            break
    return n, edges


class Vertex:
    def __init__(self, label, distance=-1):
        self.label = label
        self.distance = distance
        self.visited = False

    def brief(self):
        return self.label, self.distance

    def visit(self, from_node=None):
        self.distance = 0 if from_node is None else from_node.distance + 1
        self.visited = True


def my_bfs(graph, source):
    node_list = [Vertex(i) for i in range(len(graph))]
    source_vertex = node_list[source]
    source_vertex.visit()
    my_queue = queue.Queue()
    my_queue.put(source_vertex)
    visit_list = []
    while not my_queue.empty():
        vertex = my_queue.get()
        visit_list.append(vertex.brief())
        for label in graph[vertex.label]:
            if not node_list[label].visited:
                adjacent_vertex = node_list[label]
                adjacent_vertex.visit(vertex)
                my_queue.put(adjacent_vertex)
    return visit_list
