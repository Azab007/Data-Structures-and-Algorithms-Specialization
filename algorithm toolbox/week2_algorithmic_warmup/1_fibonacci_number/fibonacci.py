# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n
    f = [0,1]
    for i in range(2,n+1):
        f.append((f[i-2] + f[i-1]))
    return f[-1]
n = int(input())
print(calc_fib(n))
