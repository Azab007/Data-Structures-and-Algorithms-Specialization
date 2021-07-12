# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    n = len(weights)
    A = [float(v)/float(w) for v,w in zip(values,weights)]
    for i in range(0, n+1):
        if capacity == 0:
            return value
        max_val = max(A)
        w_index = A.index(max_val)
        A[w_index] = -1
        a = min(capacity, weights[w_index])
        value+= max_val * a
        capacity-= a
        weights[w_index]-= a
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
