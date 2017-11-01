from Graph import *


def main():
    graph = Graph(*Graph.input_graph())
    graph.make_adjacency_list()
    graph.make_adjacency_mat()
    print('The adjacency matrix is')
    print_matrix(graph.adjacency_mat)
    print('\nThe adjacency list is')
    print_vertex_list(graph.adjacency_list)


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
