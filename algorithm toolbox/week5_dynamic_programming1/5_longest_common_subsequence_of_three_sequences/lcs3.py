#Uses python3
import numpy
# def lcs2(a, b):
#     m = len(a)
#     n = len(b)
#     l = numpy.zeros((m+1, n+1))
#     for i in range(n):
#         l[0][i] = 0
#     for j in range(m):
#         l[j][0] = 0
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if a[i-1] == b[j-1]:
#                 l[i][j] = 1 + l[i-1][j-1]
#             else:
#                 l[i][j] = max(l[i-1][j], l[i][j-1])
#     return l[m][n]

def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    k = len(c)
    l = numpy.zeros((m+1, n+1, k+1))
    for i in range(1,m+1):
        for j in range(1,n+1):
            for k in range(1, k+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    l[i][j][k] = 1 + l[i-1][j-1][k-1]
                else:
                    l[i][j][k] = max(l[i-1][j][k], l[i][j-1][k], l[i][j][k-1])
    return l[m][n][k]




m = int(input())
a = [int(i) for i in input().split()]
n = int(input())
b = [int(i) for i in input().split()]
k = int(input())
c = [int(i) for i in input().split()]
print(int(lcs3(a, b, c)))
