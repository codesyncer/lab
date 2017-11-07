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

    def __init__(self, n_vertices, edge_list, directed=False, simple=True):
        self.n_vertices = n_vertices
        self.edge_list = edge_list
        self.directed = directed
        self.simple = simple
        self.adjacency_list = None
        self.adjacency_mat = None
        self.dfs_time = None
        self.vertices = [Graph.Vertex(i) for i in range(n_vertices)]
        self.tree_edges = []
        self.back_edges = []
        self.forward_edges = []
        self.cross_edges = []
        self.visit_list = []

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
            if u < self.n_vertices or v < self.n_vertices:
                if self.simple or v not in self.vertices[u]:
                    adjacency_list[u].append(v)
                    if not self.directed:
                        adjacency_list[v].append(u)
        self.adjacency_list = adjacency_list
        return self.vertices

    def edge(self, u, v):
        return str(u) + '-' + str(v) if self.directed else str(min(u, v)) + '-' + str(max(u, v))

    def initialize_vertices(self):
        for vertex in self.vertices:
            vertex.distance = 0
            vertex.predecessor = vertex.start_time = vertex.stop_time = None
            vertex.visited = False

    def do_dfs(self, source_label):
        self.dfs_time = 0
        self.initialize_vertices()
        self.tree_edges.clear()
        self.back_edges.clear()
        self.forward_edges.clear()
        self.cross_edges.clear()
        self.visit_list.clear()
        self.dfs(source_label)

    def dfs(self, u_label):
        u = self.vertices[u_label]
        u.visit()
        self.dfs_time += 1
        u.start_time = self.dfs_time
        self.visit_list.append(u)
        for v_label in self.adjacency_list[u_label]:
            v = self.vertices[v_label]
            if not v.visited:
                self.tree_edges.append(self.edge(u_label, v_label))
                self.visit_list.append(v)
                self.dfs(v.label)
                v.predecessor = u
            else:
                if v.stop_time is None:
                    self.back_edges.append(self.edge(u_label, v_label))
                elif u.start_time < v.start_time:
                    self.forward_edges.append(self.edge(u_label, v_label))
                else:
                    self.cross_edges.append(self.edge(u_label, v_label))
        self.dfs_time += 1
        u.stop_time = self.dfs_time
