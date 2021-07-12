# Uses python3
def get_change(m):
    count = 0
    while m >= 10:
        m = m - 10
        count+=1
    while m >= 5:
        m = m - 5
        count+=1
    while m >= 1:
        m = m - 1
        count +=1
    return count

m = int(input())
print(get_change(m))
