def pisanoPerid(m):
    prv,cur = 0,1
    for i in range(0, m*m):
        prv,cur = cur, (prv + cur) % m
        if prv == 0 and cur == 1:
            return i + 1

def fib_huge(n ,m):
    rem = n % pisanoPerid(m)
    return get_fib(rem) % m

def get_fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

n, m = map(int, input().split())
print(fib_huge(n, m))
