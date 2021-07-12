#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c

def IsBinarySearchTree(tree):
  stack = [(float('-inf'), tree[0], float('inf'))]
  while stack:
    mn,root,mx = stack.pop()
    if root.key < mn or root.key >= mx:
      return False
    if root.left != -1:
      stack.append((mn,tree[root.left],root.key))
    if root.right != -1:
      stack.append((root.key, tree[root.right], mx))
  return True


def main():
    n = int(input())
    nodes = [0 for _ in range(n)]
    for i in range(n):
        a, b, c = map(int, input().split())
        node = Node(a, b, c)
        nodes[i] = node
    if n == 0 or IsBinarySearchTree(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()
