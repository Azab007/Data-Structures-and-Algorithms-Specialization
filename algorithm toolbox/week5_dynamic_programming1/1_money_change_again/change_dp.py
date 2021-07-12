def get_change(m):
    minNumCoins = dict()
    minNumCoins[0] = 0
    for i in range(1, m+1):
        minNumCoins[i] = float('inf')
        for j in [1,3,4]:
            if i >= j:
                numCoins = minNumCoins[i - j] + 1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i] = numCoins
    return minNumCoins[m]
m = int(input())
print(get_change(m))
