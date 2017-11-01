from Graph import *


def main():
    graph = Graph(7, [(1, 2), (0, 1), (2, 3), (2, 5), (3, 5), (3, 6), (3, 4), (4, 6)])
    graph.make_adjacency_list()
    for vertex in graph.dfs_connected(2):
        print(vertex.label, end=' ')
        print('Time : ' + str(vertex.start_time) + ',' + str(vertex.stop_time))


if __name__ == '__main__':
    main()
