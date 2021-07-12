import math
# Uses python3
def operation_Num(n):
    num_of_operation = [0,0] + [math.inf]* (n-1)
    for i in range(2,n+1):
        num1,num2,num3 = [math.inf] * 3
        num1 = num_of_operation[i-1] + 1
        if i % 2 == 0:
            num2 = num_of_operation[i // 2] + 1
        if i % 3 == 0:
            num3 = num_of_operation[i // 3] + 1
        num = min(num1, num2, num3)
        num_of_operation[i] = num
    return num_of_operation


def optimal_sequence(n):
    lis = operation_Num(n)
    lis2 = [n]
    while n != 1:
        if n % 3 == 0 and lis[n] - 1 == lis[n // 3]:
            n = n //3
            lis2.append(n)
        elif n % 2 ==0 and lis[n] - 1 == lis[n // 2]:
            n = n // 2
            lis2.append(n)
        else:
            n = n-1
            lis2.append(n)
    return lis2


n = int(input())
sequence = optimal_sequence(n)
print(len(sequence) - 1)
for x in reversed(sequence):
    print(x, end=' ')
