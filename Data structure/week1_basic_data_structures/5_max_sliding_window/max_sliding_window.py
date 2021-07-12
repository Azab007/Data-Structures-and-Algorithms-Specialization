# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window_fast(seq, m):
    out = []
    stack = deque()
    for i in range(m):
        while stack and seq[i] >= seq[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(m,len(seq)):
        out.append(seq[stack[0]])
        while stack and stack[0] <= i - m:
            stack.popleft()

        while stack and seq[i] >= seq[stack[-1]]:
            stack.pop()
        stack.append(i)
    out.append(seq[stack[0]])
    return out

n = int(input())
input_sequence = [int(i) for i in input().split()]
assert len(input_sequence) == n
window_size = int(input())
print(*max_sliding_window_fast(input_sequence, window_size))