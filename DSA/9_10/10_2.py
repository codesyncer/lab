from HeavyGraph import *


def main():
    graph = Graph(5,
                  [(0, 1, 10), (0, 3, 5), (1, 2, 1), (1, 3, 2), (3, 1, 3), (3, 2, 9), (3, 4, 2), (4, 2, 4), (2, 4, 6)],
                  directed=True)
    graph.make_adjacency_list()
    # source_label = int(input('Source vertex : '))
    source_label = 0
    graph.dijkstra(source_label)
    for vertex in graph.vertices:
        print('%d is at distance %d from %d' % (vertex.label, vertex.distance, source_label))
        v = vertex
        path = [v.label]
        while v.predecessor is not None:
            v = v.predecessor
            path.append(v.label)
        print('Path : ' + str(path[::-1]))


if __name__ == '__main__':
    main()
