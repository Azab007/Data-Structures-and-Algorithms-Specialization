# Uses python3
def gcd(a, b):
    if b == 0:
        return a
    if a > b:
        c = a % b
        return gcd(b, c)
    else: 
        c = b % a
        return gcd(a, c)
def lcm_fast(a, b):
    return a*b // gcd(a, b)

a, b = map(int, input().split())
print(lcm_fast(a, b))

