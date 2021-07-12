import math
import random

def Y_closest(striped, n, d):
    min_val = d
    striped.sort(key=lambda x: x[1])
    for i in range(n):
        j = i+1
        while j < n and distance(striped[j], striped[i]) < min_val:
            min_val = distance(striped[j], striped[i])
            j+=1
    return min_val


def closestPair(sortedX, n):
    if n <=3:
        return bruteForce(sortedX, n)
    mid = n // 2
    midpoint = sortedX[mid]
    dl = closestPair(sortedX[:mid], mid)
    dr = closestPair(sortedX[mid:], n -mid)
    d = min(dl, dr)
    striped = []
    for i in range(n):
        if abs(sortedX[i][0] - midpoint[0]) < d:
            striped.append(sortedX[i])
    d_dash = Y_closest(striped, len(striped), d)
    return min(d, d_dash)



def bruteForce(P, n): 
    min_val = float('inf')  
    for i in range(n): 
        for j in range(i + 1, n): 
            if distance(P[i], P[j]) < min_val: 
                min_val = distance(P[i], P[j]) 
  
    return min_val 


def distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) * (p1[0] - p2[0])) + ((p1[1] - p2[1]) * (p1[1] - p2[1])) )

def closest(points, n):
    points.sort(key=lambda x: (x[0], x[1]))
    return closestPair(points, n)



points = list()
n = int(input())
for i in range(n):
    points.append([int(i) for i in input().split()])
'''
while True:
    n = random.randint(2,4)
    points = list()
    for i in range(n):
        points.append([int(i) for i in (random.randint(-10, 10), random.randint(-10, 10)) ])
    tst1 = bruteForce(points, n)
    tst2 = closest(points, n)
    if tst1 == tst2:
        print(str(tst1) + ' == '+ str(tst2))
    else:
        print(n)
        print(points)
        print(str(tst1) + ' != ' + str(tst2))
        break
'''

print(closest(points, n))