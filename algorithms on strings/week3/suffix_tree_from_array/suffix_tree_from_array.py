# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

class SuffixTree:
  class Node:
    def __init__(self, node, depth, start, end):
      self.parent = node
      self.children = {}
      self.depth = depth  # string depth
      self.start = start
      self.end = end
      self.visited = False
  def __init__(self, s, order, LCP):
    self.s = s
    self.chars = ['$', 'A', 'C', 'G', 'T']
    self.order = order
    self.LCP = LCP
    self.root = self.Node(None, 0, -1, -1)

  def createNewLeaf(self, node, suffix):
    leaf = self.Node(node, len(self.s) - suffix, suffix + node.depth, len(self.s))
    node.children[self.s[leaf.start]] = leaf
    return leaf

  def breakEdge(self, node, mid_start, offset):
    startChar = self.s[mid_start]
    midChar = self.s[mid_start + offset]
    midNode = self.Node(node, node.depth + offset, mid_start, mid_start + offset)
    midNode.children[midChar] = node.children[startChar]
    node.children[startChar].parent = midNode
    node.children[startChar].start+= offset
    node.children[startChar] = midNode
    return midNode

  def STfromSA(self):
    lcp_Prev = 0
    cur = self.root
    for i in range(len(self.s)):
      suffix = self.order[i]
      while cur.depth > lcp_Prev:
        cur = cur.parent
      if cur.depth == lcp_Prev:
        cur = self.createNewLeaf(cur, suffix)
      else:
        edgeStart = self.order[i-1] + cur.depth
        offset = lcp_Prev - cur.depth
        midNode = self.breakEdge(cur, edgeStart, offset)
        cur = self.createNewLeaf(midNode, suffix)
      if i < len(self.s) - 1:
        lcp_Prev = self.LCP[i]

  def printEdges(self, cur):
    cur.visited = True
    if cur != self.root:
      print(cur.start, cur.end)
    for i in range(5):
      child = cur.children.get(self.chars[i], None)
      if child is not None and not child.visited:
        self.printEdges(child)

def main():
  text = input()
  suffix_array = list(map(int, input().split()))
  lcp = list(map(int, input().split()))
  print(text)
  suffixTree = SuffixTree(text, suffix_array, lcp)
  suffixTree.STfromSA()
  suffixTree.printEdges(suffixTree.root)

threading.Thread(target=main).start()