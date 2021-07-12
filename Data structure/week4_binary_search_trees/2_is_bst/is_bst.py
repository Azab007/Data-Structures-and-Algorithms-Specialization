# #!/usr/bin/python3

# import sys, threading

# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**25)  # new thread will get stack of such size

# def IsBinarySearchTree(tree):
#   # Implement correct algorithm here
#   return True


# def main():
#   nodes = int(sys.stdin.readline().strip())
#   tree = []
#   for i in range(nodes):
#     tree.append(list(map(int, sys.stdin.readline().strip().split())))
#   if IsBinarySearchTree(tree):
#     print("CORRECT")
#   else:
#     print("INCORRECT")

# threading.Thread(target=main).start()
# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.res = []
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self, root):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.n == 0:
      self.res.append(0)
      return
    if root != -1:
      self.inOrder(self.left[root])
      self.res.append(self.key[root])
      self.inOrder(self.right[root])


def main():
  tree = TreeOrders()
  tree.read()
  tree.inOrder(0)
  arr = tree.res
  flag = 0
  if(all(arr[i] <= arr[i + 1] for i in range(len(arr)-1))): 
    flag = 1
  if flag:
    print("CORRECT")
  else:
    print("INCORRECT")


threading.Thread(target=main).start()
