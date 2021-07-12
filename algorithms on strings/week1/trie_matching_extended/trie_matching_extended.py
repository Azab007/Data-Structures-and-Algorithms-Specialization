# python3
import sys


# def build_trie(patterns):
#     tree = dict()
#     tree[0] = {}
#     i = 1
#     for pattern in patterns:
#         curRoot = tree[0]
#         for symbol in pattern:
#             if symbol in curRoot.keys():
#                 curRoot = tree[curRoot[symbol]] 
#             else:
#                 tree[i] = {}
#                 curRoot[symbol] = i
#                 curRoot = tree[i]
#                 i+=1




# 		curRoot['S'] = {}
		
#     return tree


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
		curRoot['$'] = {}
	return tree

def prefix_Trie_Matching(text, trie, indx):
	i = 0
	symbol = text[i]
	v = trie[0]
	res = -1
	while True:
		if not v or '$' in v:
			return res
		if  symbol in v:
			v = trie[v[symbol]]
			i+=1
			res = indx
			if i < len(text):
				symbol = text[i]
			elif '$' in v:
				return res
			else:
				symbol = '@'
				res = -1
		else:
			return res if '$' in v else -1



def solve (text, k, patterns):
	result = []
	trie = build_trie(patterns)
	for i in range(k):
		resu = prefix_Trie_Matching(text[i:], trie, i)
		if resu != -1:
			result.append(resu)


	return result
if __name__ == "__main__":

	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]
	k = len(text)
	ans = solve (text, k, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')
