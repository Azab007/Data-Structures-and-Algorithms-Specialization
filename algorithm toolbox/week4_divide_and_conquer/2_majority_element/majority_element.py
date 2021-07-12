# Uses python3
def get_cand(a):
    maj_index = 0
    count = 1
    for i in range(len(a)):
        if a[maj_index] == a[i]:
            count+=1
        else:
            count-=1
        if count == 0:
            maj_index = i
            count = 1
    return a[maj_index]
def is_major(a, cand):
    count = 0
    for i in range(len(a)):
        if a[i] == cand:
            count+=1
    if count > len(a) / 2:
        return True
    else:
        return False

def get_majority_element(a):
    return is_major(a, get_cand(a))

n = int(input()) 
a = list(map(int, input().split()))
if get_majority_element(a) == True:
    print(1)
else:
    print(0)
