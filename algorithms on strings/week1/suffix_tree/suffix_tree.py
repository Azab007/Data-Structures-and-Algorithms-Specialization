# python3
import sys
from collections import deque



from collections import defaultdict


def build_trie(text):

    trie = defaultdict(dict)
    i = 0
    patterns = [text[i:] for i, _ in enumerate(text)]
    for pattern in patterns:
        v = 0
        for symbol in pattern:
            if symbol in trie[v]:
                v = trie[v][symbol]
            else:
                i += 1
                trie[v][symbol] = i
                v = i
    return trie


def Suffix_tree(trie):
    result = []

    def dfs(index, text_string):
        if index not in trie and text_string:
            result.append(text_string) # If end of the tree, then append
            return
        current_branch = trie[index]
        if len(current_branch) > 1 and text_string:
            result.append(text_string) # If branching out, append till last branch and reset text string
            text_string = ""
        for symbol, ind in current_branch.items():
            dfs(ind, text_string + symbol)

    dfs(0, "")
    return result


def build_suffix_tree(text):
  trie = build_trie(text)
  return Suffix_tree(trie)


if __name__ == '__main__':
  text = input()
  result = build_suffix_tree(text)
  print("\n".join(result))