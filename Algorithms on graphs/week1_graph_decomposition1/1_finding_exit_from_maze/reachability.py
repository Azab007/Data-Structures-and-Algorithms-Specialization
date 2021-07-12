#Uses python3

import sys



def reach(adj, x, y):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            reach(adj,i,y)
    if visited[y] == True:
        return 1

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    u, v = map(int, input().split())
    # print(*adj_list)
    visited = [False] * (n_vertices + 1)
    if reach(adj_list, u, v) == 1:
        print(1)
    else:
        print(0)

