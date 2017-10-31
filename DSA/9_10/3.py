from Graph import *


def main():
    graph = Graph(*Graph.input_graph())
    components = graph.get_components()
    print_matrix(components)
    print(len(components))


def print_matrix(mat):
    for row in mat:
        print(row)


if __name__ == '__main__':
    main()
