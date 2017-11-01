from Graph import *


def main():
    graph = Graph(5, [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 3)], True)
    graph.make_adjacency_list()
    print(graph.get_cycles())


if __name__ == '__main__':
    main()
