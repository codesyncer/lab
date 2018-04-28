import queue


class Graph:
    class Vertex:
        def __init__(self, label, distance=-1):
            self.label = label
            self.distance = distance
            self.visited = False
            self.start_time = None
            self.stop_time = None
            self.predecessor = None

        def visit(self, from_node=None):
            self.distance = 0 if from_node is None else from_node.distance + 1
            self.visited = True
            self.predecessor = from_node

        def __str__(self):
            return self.label

    def __init__(self, n_vertices, edge_list, directed=False, simple=True):
        self.n_vertices = n_vertices
        self.edge_list = edge_list
        self.directed = directed
        self.simple = simple
        self.adjacency_list = None
        self.adjacency_mat = None
        self.dfs_time = None
        self.vertices = [Graph.Vertex(i) for i in range(n_vertices)]

    @staticmethod
    def input_graph():
        n = int(input('Enter the number of vertices: '))
        print('Enter the edge_list(u v):')
        edge_list = []
        while True:
            ip = input()
            try:
                u, v = tuple(ip.split())
                edge_list.append((int(u), int(v)))
            except ValueError:
                break
        return n, edge_list

    def make_adjacency_list(self):
        adjacency_list = [[] for _ in range(self.n_vertices)]
        for u, v in self.edge_list:
            if self.simple or v not in self.vertices[u]:
                adjacency_list[u].append(v)
                if not self.directed:
                    adjacency_list[v].append(u)
        self.adjacency_list = adjacency_list
        return self.vertices

    def make_adjacency_mat(self):
        mat = [[0 for _ in range(self.n_vertices)] for _ in range(self.n_vertices)]
        for u, v in self.edge_list:
            if u < self.n_vertices or v < self.n_vertices:
                mat[u][v] += 1
                if not self.directed:
                    mat[v][u] += 1
        self.adjacency_mat = mat
        return mat

    def initialize_vertices(self):
        for vertex in self.vertices:
            vertex.distance = 0
            vertex.predecessor = vertex.start_time = vertex.stop_time = None
            vertex.visited = False

    def bfs_connected(self, source_label):
        self.initialize_vertices()
        return self.bfs(source_label)

    def bfs(self, source_label):
        source_vertex = self.vertices[source_label]
        source_vertex.visit()
        my_queue = queue.Queue()
        my_queue.put(source_vertex)
        visit_list = []
        while not my_queue.empty():
            vertex = my_queue.get()
            visit_list.append(vertex)
            for label in self.adjacency_list[vertex.label]:
                v = self.vertices[label]
                if not v.visited:
                    adjacent_vertex = v
                    adjacent_vertex.visit(vertex)
                    my_queue.put(adjacent_vertex)
        return visit_list

    def get_components(self):
        self.initialize_vertices()
        component_marker = [0 for _ in range(self.n_vertices)]
        component_list = []
        component_counter = 1
        for i in range(self.n_vertices):
            if not component_marker[i]:
                connected_vertices = []
                component_marker[i] = component_counter
                for u in self.bfs(i):
                    component_marker[u.label] = component_counter
                    connected_vertices.append(u)
                component_list.append(connected_vertices)
                component_counter += 1
        return component_list, component_marker

    def get_cycles(self):
        self.initialize_vertices()
        source_vertex = self.vertices[0]
        source_vertex.visit()
        my_queue = queue.Queue()
        my_queue.put(source_vertex)
        cycles = []
        while not my_queue.empty():
            vertex = my_queue.get()
            for label in self.adjacency_list[vertex.label]:
                if not self.vertices[label].visited:
                    adjacent_vertex = self.vertices[label]
                    adjacent_vertex.visit(vertex)
                    my_queue.put(adjacent_vertex)
                else:
                    tmp = vertex
                    cycle = []
                    while tmp is not None and tmp.label != label:
                        cycle.insert(0, tmp.label)
                        tmp = tmp.predecessor
                    if tmp is None:
                        continue
                    cycle.insert(0, tmp.label)
                    cycle.insert(0, vertex.label)
                    cycles.append(cycle)
        return cycles

    def dfs_connected(self, source_label):
        self.dfs_time = 0
        self.initialize_vertices()
        return self.dfs(source_label)

    def dfs(self, u_label):
        u = self.vertices[u_label]
        u.visit()
        self.dfs_time += 1
        u.start_time = self.dfs_time
        visit_list = [u]
        for v_label in self.adjacency_list[u_label]:
            v = self.vertices[v_label]
            if not v.visited:
                visit_list += self.dfs(v.label)
                v.predecessor = u
        self.dfs_time += 1
        u.stop_time = self.dfs_time
        return visit_list
