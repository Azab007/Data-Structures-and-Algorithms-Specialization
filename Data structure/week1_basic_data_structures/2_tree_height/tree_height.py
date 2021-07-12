import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def height2(p, node, visited, height):
    if p[node] == -1:
        visited[node] = 1
        return 1
    if visited[node] == 1:
        return height[node]
    visited[node] = 1
    height[node] = 1 + height2(p, p[node], visited, height)
    return height[node]

def height1(p, n):
    max1 = 0
    visited = [0] * n
    height = [0] * n

    for i in range(n):
        if (not visited[i]):
            height[i] = height2(p, i, visited, height) 
        max1 = max(max1, height[i])
    return max1
n = int(input())
p = [int(i) for i in input().split()]

def main():
    print(height1(p, n))
threading.Thread(target=main).start()