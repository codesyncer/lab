from GraphReps import *


def main():
    graph = adjacency_list(*input_graph())
    source = int(input('Enter source vertex: '))
    print(my_bfs(graph, source))


if __name__ == '__main__':
    main()
