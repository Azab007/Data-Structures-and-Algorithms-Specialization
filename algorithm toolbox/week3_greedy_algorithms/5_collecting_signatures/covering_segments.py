# Uses python3
def optimal_points(segments):
    s = len(segments)
    points = []
    segments.sort(key= lambda x: x[1])
    index = 0
    while index < s:
        cur = segments[index]
        while index < s-1 and cur[1] >= segments[index + 1][0]:
            index+=1
        points.append(cur[1])
        index+=1
    return points

n = int(input())
segments = []
for i in range(n):
    a,b = [int(i) for i in input().split()]
    segments.append((a,b))
points = optimal_points(segments)
print(len(points))
print(*points)
