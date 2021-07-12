# Uses python3
import numpy

def edit_distance(s, t):
    len_s = len(s)
    len_t = len(t)
    d = numpy.zeros((len_s+1,len_t+1))
    for i in range(len_s+1):
        d[i][0] = i
    for j in range(len_t+1):
        d[0][j] = j

    for j in range(1,len_t+1):
        for i in range(1,len_s+1):
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)
    return int(d[len_s][len_t])
print(edit_distance(input(), input()))



