#Uses python3

import sys


def negative_cycle(adj, cost):
    len_adj = len(adj)
    dist = [-1] * len_adj
    # prev = [None] * len_adj
    dist[0] = 0
    for i in range(len_adj):
        for j in range(len_adj):
            for indx,v in enumerate(adj[j]):
                cost1 = cost[j][indx]
                if dist[v] > dist[j] + cost1:
                    dist[v] = dist[j] + cost1
                    # prev[v] = j
        if i == len_adj - 2:
            dist1 = list(dist)
        if i == len_adj - 1:
            dist2 = list(dist)
    if dist1 == dist2:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
