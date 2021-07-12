#Uses python3
import sys
import math

def Distance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  

class MinLen:
    def __init__(self, n, edges):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.edges = edges

    def Find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.Find(self.parent[i])
        return self.parent[i]

    def Union(self, i, j):
        i_parent = self.Find(i)
        j_parent = self.Find(j)
        if i_parent == j_parent:
            return
        else:
            if self.rank[i_parent] > self.rank[j_parent]:
                self.parent[j_parent] = i_parent
            else:
                self.parent[i_parent] = j_parent
                if self.rank[i_parent] == self.rank[j_parent]:
                    self.rank[j_parent] += 1
    def Kruskal(self):
        res = 0
        self.edges.sort(key=lambda x: x[2])
        for u,v,w in self.edges:
            if self.Find(u) != self.Find(v):
                res+=w
                self.Union(u,v)
        return res

if __name__ == '__main__':
    n = int(input())
    points = [None] * n
    edges = []
    for i in range(n):
        a,b = map(int, input().split())
        points[i] = (a,b)
    for i in range(n):
        (x0,y0) = points[i]
        for j in range(i+1,n):
            (x1,y1) = points[j]
            dis = Distance(x0,y0,x1,y1)
            edges.append((i,j,dis))
    minLength = MinLen(n,edges)
    result = minLength.Kruskal()
    print("{0:.9f}".format(result))
