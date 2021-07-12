from collections import deque

def isBalanced(w):
    stack = deque()
    global_index = 0
    index = 0
    for char in w:
        if char in '([{':
            stack.append(char)
            stack.append(global_index + 1)
        elif char not in ']})':
            global_index+=1
            continue
        else:
            if not stack:
                return global_index + 1
            index = stack.pop()
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '['  and char != ']'):
                return global_index + 1
        global_index+=1
    if not stack:
        return "Success"
    else:
        index = stack.pop()
        stack.pop()
        while stack:
            index = stack.pop()
            stack.pop()
        return index
w = input()
print(isBalanced(w))


