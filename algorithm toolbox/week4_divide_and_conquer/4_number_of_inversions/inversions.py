# Uses python3
total_count = 0
def merge(left, right):
    i = 0
    j = 0
    inv_counter = 0
    arr = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i = i+1
        else:
            arr.append(right[j])
            inv_counter+= len(left) - i
            j = j+1
    arr += left[i:]
    arr += right[j:]
    return arr, inv_counter

def mergesort(arr):
    global total_count
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    sortedArray, count = merge(left, right)
    total_count+= count
    return sortedArray

n = int(input())
a = [int(i) for i in input().split()]
mergesort(a)
print(total_count)
