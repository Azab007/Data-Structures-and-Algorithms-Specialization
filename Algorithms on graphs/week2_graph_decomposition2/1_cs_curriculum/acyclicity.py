#Uses python3

import sys

cycle = False
def reach(adj, x, y):
    global cycle
    visited[x] = True
    if y in adj[x]:
        cycle = True
        return
    for i in adj[x]:
        if not visited[i]:
            reach(adj,i, y)




def number_of_components(adj):
    global cycle
    for i in range(1,len(adj)):
        if not visited[i]:
            reach(adj, i, i)
    if cycle:
        print(1)
    else:
        print(0)
    


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adj_list[a].append(b)
    visited = [False] * (n_vertices + 1)
    number_of_components(adj_list)    
