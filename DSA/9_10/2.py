from Graph import *


def main():
    graph = Graph(*Graph.input_graph())
    graph.make_adjacency_list()
    source = input('Enter source vertex: ')
    for vertex in graph.bfs_connected(int(source)):
        print(str(vertex.label) + ' @ distance ' + str(vertex.distance) + ' from ' + source)


if __name__ == '__main__':
    main()
