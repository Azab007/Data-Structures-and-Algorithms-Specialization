# Uses python3
def get_fibonacci_last_digit_fast(n):
    if (n <= 1):
        return n
    f = [0,1]
    for i in range(2,n+1):
        f.append((f[i-2] + f[i-1]) % 10)
    return f[-1]

def fib_sum_sqr(n):
    n = n % 60
    a = get_fibonacci_last_digit_fast(n)
    b = get_fibonacci_last_digit_fast(n + 1)
    return (a * b) % 10

n = int(input())
print(fib_sum_sqr(n))
