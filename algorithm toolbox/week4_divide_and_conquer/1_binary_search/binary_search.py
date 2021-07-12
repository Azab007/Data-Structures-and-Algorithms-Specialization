def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid =left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1

arr = list(map(int, input().split()))
k = list(map(int, input().split()))
arr1 = arr[1:]
k1 = k[1:]
for x in k1:
        # replace with the call to binary_search when implemented
    print(binary_search(arr1, x), end = ' ')
    #print(x, end=' ')
