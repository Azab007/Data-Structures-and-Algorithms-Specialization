# python3

import sys
import random
from collections import deque

m = (10 ** 9) + 7
x = random.randint(1,10**9)
count = 0

# def binary_search(k,starting_index, h1, h2, len_text, len_pattern):
# 	l = 0
# 	r = len_text
# 	mid_text = (starting_index + len_pattern) // 2
# 	mid_pattern = len_pattern // 2
# 	while l <= r:
# 	if (h1[mid_text + 1] - (pow(x1, 1) * h1[mid_text])) != (h2[mid_pattern + 1] - (pow(x1, 1) * h2[mid_pattern])):
# 		count+=1

# 	else:
# 		if (h1[starting_index + mid_text] - (pow(x1, mid_text) * h1[starting_index]) != (h2[mid_pattern] - ((pow(x1, mid_pattern)) * h2[mid_pattern])):
# 			binary_search(starting_index, h1, h2, len_text - mid_text, len_pattern - mid_pattern )

# 		if (h1[mid_text] - (pow(x1, mid_pattern) * h1[starting_index]) != (h2[mid_pattern] - ((pow(x1, mid_pattern)) * h2[mid_pattern]))



def value(hash_table, prime, x, start, length):
    y = pow(x, length, prime)
    hash_value = (hash_table[start + length] - y * hash_table[start]) % prime
    return hash_value


def check(a_start, length, p_len, k):
    global m, h1, h2
    stack = deque()
    stack.append((a_start, 0, length, 1))
    stack.append((a_start+length, length, p_len-length, 1))
    count = 0
    temp = 2
    C = 0
    while stack:
        a, b, L, n = stack.popleft()
        u1 = value(h1, m, x, a, L)
        v1 = value(h2, m, x, b, L)
        if temp != n:
            count = C
        if u1 != v1:
            count += 1
            if L > 1:
                stack.append((a, b, L//2, n+1))
                stack.append((a + L//2, b + L//2, L - L//2, n+1))
            else:
                C += 1
        if count > k:
            return False
        temp = n
    if count > k:
        return False
    else:
        return True

def solve(k, text, pattern):
	global h1, h2
	sol = []
	len_text = len(text)
	len_pattern = len(pattern)

	h1 = [0] * (len_text + 1)

	h2 = [0] * (len_pattern + 1)
	
	for i in range(1, len_text+1):
		h1[i] = (x * h1[i-1] + ord(text[i-1])) % m
	for i in range(1, len_pattern+1):
		h2[i] = (x * h2[i-1] + ord(pattern[i-1])) % m

	for i in range(len_text-len_pattern+1):
		if check(i, len_pattern // 2, len_pattern, k):
			sol.append(i)

	return sol

for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
