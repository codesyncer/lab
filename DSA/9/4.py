from GraphReps import *


def main():
    graph = adjacency_list(5, [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 3)], True)
    print(get_cycles(graph))


def get_cycles(graph):
    node_list = [Vertex(i) for i in range(len(graph))]
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
                if node_list[label] == vertex.pred:
                    continue
                v1 = node_list[label]
                v2 = vertex
                cycle = []
                if node_list[label].distance != vertex.distance:
                    v1 = v1.pred
                    cycle.append(label)
                while v1 != v2:
                    cycle.insert(0, v1.label)
                    cycle.append(v2.label)
                    # if v1.label in graph[v2.label]:
                    #     cycles.append(cycle)
                    v1 = v1.pred
                    v2 = v2.pred
                cycle.append(v1.label)
                cycles.append(cycle)
    return cycles


if __name__ == '__main__':
    main()
