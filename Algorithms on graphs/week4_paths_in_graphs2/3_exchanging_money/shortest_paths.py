#Uses python3

import sys
from collections import deque

def BellmanFord(n, graph, adj, s):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    neg_cycle = deque()
    for i in range(n):
        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == n - 1:
                    neg_cycle.append(v)

    visited = [False] * (n + 1)
    while neg_cycle:
        u = neg_cycle.popleft()
        visited[u] = True
        dist[u]= '-'
        for v in adj[u]:
            if not visited[v]:
                neg_cycle.append(v)
    return dist

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adjacency_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))
        adjacency_list[a].append(b) 
    start = int(input())
    distance = BellmanFord(n_vertices, edges, adjacency_list, start)
    for dist in distance[1:]:
        if dist == float('inf'):
            print('*')
        else:
            print(dist)