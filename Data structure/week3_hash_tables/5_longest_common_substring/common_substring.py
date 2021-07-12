# python3

import random
import sys
prime1 = 1000000007
x1 = random.randint(1,10**9)
prime2 = 1000004249
x2 = random.randint(1,10**9)

def binary_search(s1, s2):
	l = 0
	r = min(len(s1), len(s2))
	b = 0
	c = 0
	while l<=r:
		mid = (l + r) // 2
		a = compare_hashes(s1, s2, mid)
		if a[0]:
			b = a[1]
			c = a[2]
			l = mid + 1
		else:
			r = mid - 1
	if r < 0:
		r = 0
	return [b, c, r]

def compare_hashes(s1, s2, mid):
	hashes_s = precompute_hashes(s, mid,prime1,x1)
	hashes_t = precompute_hashes(t, mid,prime1,x1)
	hash_table1 = {}
	j = 0
	for i in hashes_t:
		hash_table1[i] = j
		j+=1
	for index, _hash in enumerate(hashes_s):
		if _hash in hash_table1:
			if s[index:index + mid] == t[hash_table1[_hash]:hash_table1[_hash]+mid]:
				return [True, index, hash_table1[_hash]]
	return [False, 0, 0]




  

def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, pattern_len, p, x):
    H = [0] * (len(text) - pattern_len + 1)
    s = text[-pattern_len:]
    H[len(text)-pattern_len] = poly_hash(s, p, x)
    y = 1
    for i in range(1, pattern_len+1):
        y = (y * x) % p
    for i in reversed(range(len(text) - pattern_len)):
        pre_hash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])
        while(pre_hash < 0):
            pre_hash += p
        H[i] = pre_hash % p
    return H




for line in sys.stdin.readlines():
	s, t = line.split()
	print(*binary_search(s,t))

