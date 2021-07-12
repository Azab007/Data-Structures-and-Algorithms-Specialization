# Uses python3
import sys
import unittest
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


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


n = int(input())
print(fibonacci_sum_fast(n))
