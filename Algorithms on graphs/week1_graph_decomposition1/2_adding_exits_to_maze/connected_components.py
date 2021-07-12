#Uses python3

import sys

def reach(adj, x):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            reach(adj,i)

def number_of_components(adj):
    result = 0
    for i in range(1, len(adj)):
        if not visited[i]:
            reach(adj, i)
            result+=1
    return result

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    visited = [False] * (n_vertices + 1)

    print(number_of_components(adj_list))
