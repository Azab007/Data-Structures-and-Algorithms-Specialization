import random

st = input()
q = int(input())
len_st = len(st)
m1 = (10 ** 9) + 7
m2 = (10 ** 9) + 9
x = random.randint(1,10**9)
h1 = [0] * (len_st + 1)
h2 = [0] * (len_st + 1)

for i in range(1, len_st+1):
	h1[i] = (x * h1[i-1] + ord(st[i-1])) % m1
	h2[i] = (x * h2[i-1] + ord(st[i-1])) % m2

for i in range(q):
	a,b,l = map(int, input().split())
	if ( (h1[a + l] - (pow(x,l,m1) * h1[a])) % m1 == (h1[b + l] - (pow(x,l,m1) * h1[b])) % m1 )  and ( (h2[a + l] - (pow(x,l,m2) * h2[a])) % m2 == (h2[b + l] - (pow(x,l,m2) * h2[b])) % m2):
		print('Yes')
	else:
		print('No')
