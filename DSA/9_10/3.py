from Graph import *


def main():
    graph = Graph(*Graph.input_graph())
    graph.make_adjacency_list()
    components_list, component_markers = graph.get_components()
    for component in components_list:
        for vertex in component:
            print(str(vertex.label) + ' belongs to component ' + str(component_markers[vertex.label]))


def print_matrix(mat):
    for row in mat:
        print(row)


if __name__ == '__main__':
    main()
