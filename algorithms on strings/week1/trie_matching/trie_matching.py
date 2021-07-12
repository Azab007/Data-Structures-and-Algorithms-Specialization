# python3
import sys

# NA = -1

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    i = 1
    for pattern in patterns:
        curRoot = tree[0]
        for symbol in pattern:
            if symbol in curRoot.keys():
                curRoot = tree[curRoot[symbol]] 
            else:
                tree[i] = {}
                curRoot[symbol] = i
                curRoot = tree[i]
                i+=1
                
    return tree

def prefix_Trie_Matching(text, trie):
	i = 0
	symbol = text[i]
	v = trie[0]
	while True:
		if not v:
			return True
		elif  symbol in v.keys():
			v = trie[v[symbol]]
			i+=1
			if i < len(text):
				symbol = text[i]
			else:
				symbol = '$'
		else:
			return False



def solve (text, k, patterns):
	result = []
	trie = build_trie(patterns)
	for i in range(k):
		if prefix_Trie_Matching(text[i:], trie):
			result.append(i)


	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]
k = len(text)
ans = solve (text, k, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
