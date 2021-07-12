#Uses python3

import sys, threading

sys.setrecursionlimit(200000)

clock = 1
def explore_clock(adj, x, visited, postOrder):
    global clock
    visited[x] = True
    clock+=1
    for i in adj[x]:
        if not visited[i]:
            explore_clock(adj,i, visited, postOrder)
    postOrder[x] = clock
    clock+=1

def DFS(adj):
    visited = [False] * (n_vertices + 1)
    postOrder = [0] * (n_vertices + 1)
    for i in range(1,n_vertices+1):
        if not visited[i]:
            explore_clock(adj, i, visited, postOrder)
    # postOrder = list(enumerate(postOrder[1:], start=1))
    postOrder.sort(key=lambda x: x[1], reverse=True)
    postV = []
    for v, post in postOrder:
        postV.append(v)
    return postV 



def explore(adj, x, visited):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            explore(adj,i, visited)


def number_of_strongly_connected_components(rev_adj, adj):
    result = 0
    postV = DFS(rev_adj)
    visited = [False] * (n_vertices + 1)
    for v in postV:
        if not visited[v]:
            explore(adj, v, visited)
            result+=1
    return result

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    adj_list = [[] for _ in range(n_vertices + 1)]
    rev_adj_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a, b) in edges:
        adj_list[a].append(b)
        rev_adj_list[b].append(a)
    
    print(number_of_strongly_connected_components(rev_adj_list, adj_list))
