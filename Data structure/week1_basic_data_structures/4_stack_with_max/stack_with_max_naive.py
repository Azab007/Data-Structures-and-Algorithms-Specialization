#python3
stack = []
aux_stack = []
output = []
n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == "push":
        stack.append(int(query[1]))
        if not aux_stack:
            aux_stack.append(int(query[1]))
        else:
            mx = max(int(query[1]), aux_stack[-1])
            aux_stack.append(mx)
    elif query[0] == "pop":
        stack.pop()
        aux_stack.pop()
    elif query[0] == "max":
        output.append(aux_stack[-1])
    else:
        assert(0)

for num in output:
    print(num)
