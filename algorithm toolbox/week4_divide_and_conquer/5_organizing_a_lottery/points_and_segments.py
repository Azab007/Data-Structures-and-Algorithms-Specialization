arr = []
num_of_points, points1 = [int(i) for i in input().split()]

for i in range(num_of_points):
    a, b = [int(i) for i in input().split()]
    arr.append((a,'l'))
    arr.append((b,'r'))

points = input().split()
for i in points:
    arr.append((int(i),'p'))
arr.sort()
segm_count = 0
dic = dict()
for point in arr:
    if point[1] == 'l':
        segm_count+=1
    elif point[1] == 'r':
        segm_count-=1
    else:
        dic[point[0]] = segm_count        


for x in points:
    print(dic[int(x)], end=' ')
