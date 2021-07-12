# Uses python3
def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n
    f = [0,1]
    for i in range(2,n+1):
        f.append((f[i-2] + f[i-1]) % 10)
    return f[-1]
n = int(input())
print(get_fibonacci_last_digit_naive(n))
