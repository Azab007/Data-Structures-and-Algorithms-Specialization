#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for _ in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, v, parent ,D):
    if D[v] == -1:
        if len(tree[v].children) == 1 and v != 0:
            D[v] = tree[v].weight
        else:
            m1 = tree[v].weight
            for u in tree[v].children:
                if u != parent:
                    for j in tree[u].children:
                        if j!=v:
                            m1+=dfs(tree,j,u,D)
            m0 = 0
            for u in tree[v].children:
                if u != parent:
                    m0+=dfs(tree,u,v,D)
            D[v] = max(m0,m1)
    return D[v]
    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    D = [-1] * size
    return dfs(tree, 0, -1,D)


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
