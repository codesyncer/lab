from Graph import *


def main():
    graph = Graph(8, [(0, 2), (2, 3), (2, 1), (2, 6), (3, 0), (4, 2), (5, 2), (5, 7), (6, 1), (6, 7), (7, 4)], True)
    graph.make_adjacency_list()
    print(graph.get_cycles())


if __name__ == '__main__':
    main()
