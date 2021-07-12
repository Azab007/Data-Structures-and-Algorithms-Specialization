# python3

import itertools
clauses = []

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
positions = range(1,n+1)
adj = [[] for _ in range(n)]

for i,j in edges:
    adj[i-1].append(j-1)
    adj[j-1].append(i-1)

def varNum(i,j):
    return n*i + j

def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

for i in range(n):
    exactly_one_of([varNum(i,j) for j in positions])    

for j in positions:
    exactly_one_of([varNum(i,j) for i in range(n)])

for j in positions[:-1]:
    for i,nodes in enumerate(adj):
        clauses.append([-varNum(i,j)] + [varNum(n,j+1) for n in nodes])

print(len(clauses), n*n)
for c in clauses:
    c.append(0)
    print(' '.join(map(str, c)))
