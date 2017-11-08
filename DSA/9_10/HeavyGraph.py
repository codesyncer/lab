from MinHeap import *


class Graph:
    class Vertex:
        def __init__(self, label, distance=-1):
            self.label = label
            self.distance = distance
            self.predecessor = None
            self.index = None

        def __lt__(self, other):
            return self.distance < other.distance

        def __gt__(self, other):
            return self.distance > other.distance

    def __init__(self, n_vertices, edge_list, directed=False, simple=True):
        self.n_vertices = n_vertices
        self.edge_weight = {}
        self.directed = directed
        self.edge_list = self.process(edge_list)
        self.simple = simple
        self.adjacency_list = None
        self.vertices = [Graph.Vertex(i) for i in range(n_vertices)]
        self.inf = 1000

    def edge(self, u, v):
        return str(u) + '-' + str(v) if self.directed else str(min(u, v)) + '-' + str(max(u, v))

    def process(self, edge_list):
        new_edge_list = []
        for u, v, duv in edge_list:
            self.edge_weight[self.edge(u, v)] = duv
            new_edge_list.append((u, v))
        return new_edge_list

    def input_graph(self):
        n = int(input('Enter the number of vertices: '))
        print('Enter the edge_list(u v weight):')
        edge_list = []
        while True:
            ip = input()
            try:
                u, v, duv = tuple(ip.split())
                u = int(u)
                v = int(v)
                edge_list.append((u, v))
                self.edge_weight[self.edge(u, v)] = duv
            except ValueError:
                break
        self.edge_list = edge_list
        self.n_vertices = n
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

    def dijkstra(self, source_label):
        for vertex in self.vertices:
            vertex.distance = self.inf
            vertex.predecessor = None
        source_vertex = self.vertices[source_label]
        source_vertex.distance = 0
        priority_queue = MinHeap(self.vertices[:])
        while not priority_queue.empty():
            w = priority_queue.extract_min()
            for v_label in self.adjacency_list[w.label]:
                v = self.vertices[v_label]
                dwv = self.edge_weight[self.edge(w.label, v.label)]
                if v.distance == self.inf or w.distance + dwv < v.distance:
                    v.distance = w.distance + dwv
                    v.predecessor = w
                    priority_queue.update_priority(v.index)
            # priority_queue.build_heap(priority_queue.arr)
