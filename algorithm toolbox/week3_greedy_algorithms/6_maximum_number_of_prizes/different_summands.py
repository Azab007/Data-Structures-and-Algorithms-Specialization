# Uses python3
def optimal_summands(n):
    summands = []
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    i = 1
    while (n - ((i/2)* (1 + i)) >= i+1):
        summands.append(i)
        i+=1
    i-=1
    summands.append(n - ((i/2)* (1 + i)))
    return summands


n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(int(x), end=' ')
