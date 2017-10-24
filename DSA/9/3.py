from GraphReps import *


def main():
    graph = adjacency_list(*input_graph())
    visited = [False for _ in range(len(graph))]
    component_count = 0
    for i in range(len(graph)):
        if not visited[i]:
            vertices = []
            visited[i] = True
            for u, _ in my_bfs(graph, i):
                visited[u] = True
                vertices.append(u)
            component_count += 1
            print(vertices)
    print(component_count)


if __name__ == '__main__':
    main()
