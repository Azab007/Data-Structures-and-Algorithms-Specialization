# python3
def read_input():
    return (input().rstrip(), input().rstrip())


def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, len_p, p, x):
    H = [0] * (len(text) - len_p + 1)
    s = text[-len_p:]
    H[len(text)-len_p] = poly_hash(s, p, x)
    y = 1
    for i in range(1, len_p+1):
        y = (y * x) % p
    for i in reversed(range(len(text) - len_p)):
        temp = x * H[i + 1] + ord(text[i]) - y * ord(text[i + len_p])
        while(temp < 0):
            temp += p
        H[i] = temp % p
    return H

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    res = []
    prime = 1000000007 
    x = 263
    len_pattern = len(pattern)
    len_text = len(text)
    pHash = poly_hash(pattern, prime, x)
    H = precompute_hashes(text, len_pattern, prime, x)
    for i in range((len_text - len_pattern) + 1):
        if pHash != H[i]:
            continue
        if text[i: i+len_pattern] == pattern:
            res.append(i)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

