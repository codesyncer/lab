from GraphReps import *


def main():
    n, edges = input_graph()
    print('The adjacency matrix is')
    print_matrix(adjacency_mat(n, edges))
    print('\nThe adjacency list is')
    print_vertex_list(adjacency_list(n, edges))


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
