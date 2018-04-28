from Graph import *


def main():
    # graph = Graph(7, [(1, 2), (0, 1), (2, 3), (2, 5), (3, 5), (3, 6), (3, 4), (4, 6)])
    graph = Graph(10, [(1, 2), (1, 3), (2, 4), (4, 5), (4, 6), (5, 7), (7, 8), (8, 9), (9, 3), (3, 1), (3, 0)])
    graph.make_adjacency_list()
    for vertex in graph.dfs_connected(1):
        print(vertex.label, end=' ')
        print('Time : ' + str(vertex.start_time) + ',' + str(vertex.stop_time))


if __name__ == '__main__':
    main()
