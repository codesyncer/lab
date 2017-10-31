from Graph import *


def main():
    graph = Graph(7, [(1, 2), (0, 1), (2, 3), (2, 5), (3, 5), (3, 6), (3, 4), (4, 6)])
    for vertex in graph.connected_dfs(2):
        print(vertex.label, end=' ')
        print('Time : ' + str(vertex.time))


if __name__ == '__main__':
    main()
