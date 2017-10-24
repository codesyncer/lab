from GraphReps import *


def main():
    graph = adjacency_list(*input_graph(), True)


class Node(Vertex):
    def __init__(self, label):
        Vertex.__init__(self, label)
        self.predecessor = None


def get_cycles(graph):
    node_list = [Node(i) for i in range(len(graph))]
    source_vertex = node_list[0]
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
                adjacent_vertex.predecessor = vertex
                my_queue.put(adjacent_vertex)
            else:
                pass
    return visit_list


if __name__ == '__main__':
    main()
