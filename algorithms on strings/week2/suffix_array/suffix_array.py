# python3
import sys
from collections import defaultdict


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  suffix = []
  for i in range(len(text)):
    suffix.append((text[i:], i))
  suffix.sort()
  for arr, indx in suffix:
    print(indx, end=' ')


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  build_suffix_array(text)
  
