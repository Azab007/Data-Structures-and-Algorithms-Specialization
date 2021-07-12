# python3
swaps = []
def siftDown(arr, i):
    minIndex = i
    l = (2 * i) + 1
    if l < len(arr) and arr[l] < arr[minIndex]:
        minIndex = l
    r = (2 * i) + 2
    if r < len(arr) and arr[r] < arr[minIndex]:
        minIndex = r
    if i != minIndex:
        arr[i], arr[minIndex] = arr[minIndex], arr[i] 
        swaps.append((i, minIndex))
        siftDown(arr,minIndex)

def build_heap(data):
    for i in range((len(data) // 2) -1 , -1, -1):
        siftDown(data,i)



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
