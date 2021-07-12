# Uses python3
import numpy

def partition3(W, n, w):
    cnt = 0
    val = numpy.zeros((W+1, n+1))
    for i in range(1,W+1):
        for j in range(1,n+1):
            val[i][j] = val[i][j-1]
            if i >= w[j-1]:
                tmp = val[i - w[j-1]][j-1] + w[j-1]
                if tmp > val[i][j]:
                    val[i][j] = tmp
            if val[i][j] == W:
                cnt+=1
    if cnt < 3:
        print(0)
    else:
        print(1)



n = int(input())
w = [int(i) for i in input().split()]
sm = sum(w)
if n < 3:
    print(0)
elif sm % 3 !=0:
    print(0)
else:
    partition3(sm // 3, n, w)