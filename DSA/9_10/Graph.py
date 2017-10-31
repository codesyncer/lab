import queue


class Graph:
    class Vertex:
        def __init__(self, label, distance=-1):
            self.label = label
            self.distance = distance
            self.visited = False
            self.predecessor = None

        def brief(self):
            return self.label, self.distance

        def visit(self, from_node=None):
            self.distance = 0 if from_node is None else from_node.distance + 1
            self.visited = True
            self.predecessor = from_node

    class Node:
        def __init__(self, label, distance=-1):
            self.label = label
            self.time = None
            self.visited = False
            self.predecessor = None

        def visit(self, from_node=None):
            self.visited = True
            self.predecessor = from_node

        def start(self, time):
            self.time = (time,)

        def stop(self, time):
            self.time = (self.time[0], time)

    def __init__(self, vertex_c, edges, directed=False, simple=True):
        self.vertex_c = vertex_c
        self.edge_list = edges
        self.directed = directed
        self.simple = simple
        self.adjacency_list = None
        self.adjacency_mat = None
        self.dfs_time = None

    @staticmethod
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

    def adjacent_vertices(self, label):
        if self.adjacency_list is None:
            self.adjacency_list = Graph.gen_adjacency_list(self.vertex_c, self.edge_list, self.directed, self.simple)
        return self.adjacency_list[label]

    def get_adjacency_mat(self):
        if self.adjacency_mat is None:
            self.adjacency_mat = Graph.gen_adjacency_mat(self.vertex_c, self.edge_list, self.directed)
        return self.adjacency_mat

    def get_adjacency_list(self):
        if self.adjacency_list is None:
            self.adjacency_list = Graph.gen_adjacency_list(self.vertex_c, self.edge_list, self.directed, self.simple)
        return self.adjacency_list

    @staticmethod
    def gen_adjacency_list(vertex_c, edges, directed=False, simple=True):
        node_list = [[] for _ in range(vertex_c)]
        for u, v in edges:
            if u < vertex_c or v < vertex_c:
                if simple or v not in node_list[u]:
                    node_list[u].append(v)
                    if not directed:
                        node_list[v].append(u)
        return node_list

    @staticmethod
    def gen_adjacency_mat(vertex_c, edges, directed=False):
        mat = [[0 for _ in range(vertex_c)] for _ in range(vertex_c)]
        for u, v in edges:
            if u < vertex_c or v < vertex_c:
                mat[u][v] += 1
                if not directed:
                    mat[v][u] += 1
        return mat

    def connected_bfs(self, src_label):
        graph = self.get_adjacency_list()
        node_list = [Graph.Vertex(i) for i in range(len(graph))]
        return self.pre_initialized_bfs(node_list, src_label)

    def pre_initialized_bfs(self, node_list, src_label):
        src_label_vertex = node_list[src_label]
        src_label_vertex.visit()
        my_queue = queue.Queue()
        my_queue.put(src_label_vertex)
        visit_list = []
        while not my_queue.empty():
            vertex = my_queue.get()
            visit_list.append(vertex.brief())
            for label in self.adjacent_vertices(vertex.label):
                v = node_list[label]
                if not v.visited:
                    adjacent_vertex = v
                    adjacent_vertex.visit(vertex)
                    my_queue.put(adjacent_vertex)
        return visit_list

    def get_components(self):
        graph = self.get_adjacency_list()
        node_list = [Graph.Vertex(i) for i in range(len(graph))]
        visited = [False for _ in range(len(graph))]
        component_list = []
        for i in range(len(graph)):
            if not visited[i]:
                vertices = []
                visited[i] = True
                for u, _ in self.pre_initialized_bfs(node_list, i):
                    visited[u] = True
                    vertices.append(u)
                component_list.append(vertices)
        return component_list

    def get_cycles(self):
        graph = self.get_adjacency_list()
        node_list = [Graph.Vertex(i) for i in range(len(graph))]
        source_vertex = node_list[0]
        source_vertex.visit()
        my_queue = queue.Queue()
        my_queue.put(source_vertex)
        cycles = []
        while not my_queue.empty():
            vertex = my_queue.get()
            for label in graph[vertex.label]:
                if not node_list[label].visited:
                    adjacent_vertex = node_list[label]
                    adjacent_vertex.visit(vertex)
                    my_queue.put(adjacent_vertex)
                else:
                    if node_list[label] == vertex.predecessor:
                        continue
                    v1 = node_list[label]
                    v2 = vertex
                    cycle = []
                    if node_list[label].distance != vertex.distance:
                        v1 = v1.predecessor
                        cycle.append(label)
                    while v1 != v2:
                        cycle.insert(0, v1.label)
                        cycle.append(v2.label)
                        # if v1.label in graph[v2.label]:
                        #     cycles.append(cycle)
                        v1 = v1.predecessor
                        v2 = v2.predecessor
                    cycle.append(v1.label)
                    cycles.append(cycle)
        return cycles

    def connected_dfs(self, src_label):
        graph = self.get_adjacency_list()
        node_list = [Graph.Node(i) for i in range(len(graph))]
        self.dfs_time = 0
        return self.dfs(node_list, src_label)

    def get_time(self):
        self.dfs_time += 1
        return self.dfs_time

    def dfs(self, node_list, u_label):
        u = node_list[u_label]
        u.visit()
        u.start(self.get_time())
        visit_list = [u]
        for v_label in self.adjacent_vertices(u_label):
            v = node_list[v_label]
            if not v.visited:
                visit_list += self.dfs(node_list, v.label)
                v.predecessor = u
        u.stop(self.get_time())
        return visit_list
