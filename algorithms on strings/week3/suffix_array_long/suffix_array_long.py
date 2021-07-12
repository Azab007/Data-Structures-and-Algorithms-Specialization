# python3
import sys

def SortCharacters(S):
  order = [0] * len(S)
  count = {'$':0,'A': 0, 'C': 0, 'G': 0, 'T': 0 }
  for i in range(len(S)):
    count[S[i]]+=1
  chars = ['$','A', 'C', 'G', 'T']
  for i in range(1,5):
    count[chars[i]] += count[chars[i-1]]
  for i in range(len(S)-1,-1,-1):
    c = S[i]
    count[c]-=1
    order[count[c]] = i
  return order


def computeCharClasses(S, order):
  _class = [0] * len(S)
  _class[order[0]] = 0
  for i in range(1,len(S)):
    if S[order[i]] != S[order[i-1]]:
      _class[order[i]] = _class[order[i-1]] + 1
    else:
      _class[order[i]] = _class[order[i-1]]
  return _class

def sortDoubled(S,L,order,_class):
  count = [0] * len(S)
  newOrder = [0] * len(S)
  for i in range(len(S)):
    count[_class[i]]+=1
  for j in range(1,len(S)):
    count[j]+=count[j-1]
  for i in range(len(S)-1,-1,-1):
    start = (order[i] - L + len(S)) % len(S)
    cl = _class[start]
    count[cl]-=1
    newOrder[count[cl]] = start
  return newOrder


def updateClasses(newOrder, _class, L):
  n = len(newOrder)
  newClass = [0] * n
  newClass[newOrder[0]] = 0
  for i in range(1,n):
    cur = newOrder[i]
    prev = newOrder[i-1]
    mid = (cur + L) % n
    midPrev = (prev+L) % n
    if _class[cur] != _class[prev] or _class[mid] != _class[midPrev]:
      newClass[cur] = newClass[prev] + 1
    else:
      newClass[cur] = newClass[prev]
  return newClass


def build_suffix_array(S):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = SortCharacters(S)
  _class = computeCharClasses(S, order)
  L = 1
  while L < len(S):
    order = sortDoubled(S,L,order,_class)
    _class = updateClasses(order,_class,L)
    L = 2 * L
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(*build_suffix_array(text), end=' ')
