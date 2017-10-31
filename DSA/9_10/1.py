from Graph import *


def main():
    graph = Graph(*Graph.input_graph())
    print('The adjacency matrix is')
    print_matrix(graph.get_adjacency_mat())
    print('\nThe adjacency list is')
    print_vertex_list(graph.get_adjacency_list())


def print_matrix(mat):
    for row in mat:
        print(row)


def print_vertex_list(vertex_list):
    i = 0
    for vertices in vertex_list:
        print('Vertex ' + str(i) + ': ' + str(vertices)[1:-1])
        i += 1


if __name__ == '__main__':
    main()
