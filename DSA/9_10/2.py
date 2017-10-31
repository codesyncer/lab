from Graph import *


def main():
    graph = Graph(*Graph.input_graph())
    source = int(input('Enter source vertex: '))
    print(graph.connected_bfs(source))


if __name__ == '__main__':
    main()
