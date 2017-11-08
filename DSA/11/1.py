from Graph import *

if __name__ == '__main__':
    graph = Graph(8, [(0, 1), (0, 4), (0, 7), (1, 2), (2, 4), (2, 3), (2, 5), (4, 1), (4, 3), (5, 3), (6, 5), (6, 0),
                      (7, 6)],
                  directed=True)
    graph.make_adjacency_list()
    graph.do_dfs(0)
    for vertex in graph.visit_list:
        print(vertex.label, end=' ')
        print('Time : ' + str(vertex.start_time) + ',' + str(vertex.stop_time))
    print()
    print('Tree edges: ', graph.tree_edges)
    print('Back edges: ', graph.back_edges)
    print('Forward edges: ', graph.forward_edges)
    print('Cross edges: ', graph.cross_edges)
