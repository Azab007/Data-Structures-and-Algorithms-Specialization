# Uses python3

def get_fibonacci_last_digit_fast(n):
    if (n <= 1):
        return n
    f = [0,1]
    for i in range(2,n+1):
        f.append((f[i-2] + f[i-1]) % 10)
    return f[-1]

def fibonacci_sum_fast(n):
    n = (n + 2) % 60
    c = get_fibonacci_last_digit_fast(n)
    if c == 0 :
        c = 9
        return c
    return c - 1
def fibonacci_partial_sum_fast(from_, to):
    fir = fibonacci_sum_fast(to) 
    sec = fibonacci_sum_fast(from_ - 1)
    if fir >= sec:
        return fir - sec
    else:
        return (10 + fir) - sec




from_, to = map(int, input().split())
print(fibonacci_partial_sum_fast(from_, to))