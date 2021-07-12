# Uses python3
import numpy

def optimal_weight(W,n, w):
    val = numpy.zeros((W+1, n+1))
    for i in range(1,W+1):
        for j in range(1,n+1):
            val[i][j] = val[i][j-1]
            if i >= w[j-1]:
                tmp = val[i - w[j-1]][j-1] + w[j-1]
                if tmp > val[i][j]:
                    val[i][j] = tmp
    return val[W][n]

W, n = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]

print(int(optimal_weight(W,n, w)))
