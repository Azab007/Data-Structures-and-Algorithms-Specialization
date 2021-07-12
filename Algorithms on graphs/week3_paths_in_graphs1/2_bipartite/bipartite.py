#Uses python3

import sys
from queue import Queue
def BFS(adj, s):
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(len(adj[u])):
            if dist[u] == dist[adj[u][i]]:
                return 0
        for v in adj[u]:
            if dist[v] == float('inf'):
                Q.put(v)
                dist[v] = dist[u] + 1
    return 1


def bipartite(adj):
    return BFS(adj, 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
