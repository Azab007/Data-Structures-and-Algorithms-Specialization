def IsGreaterOrEqual(digit, max_digit):
    num1 = str(digit)+str(max_digit)
    num2 = str(max_digit)+str(digit)
    return int(num1)>=int(num2)

def largest_number(a):
    res = []
    while a != []:
        max_digit = 0
        for x in a:
            if IsGreaterOrEqual(x,max_digit):
                max_digit = x
        res.append(max_digit)
        a.remove(max_digit)
    return res
b = int(input())
a = [int(i) for i in input().split()]
print(''.join(str(i) for i in largest_number(a)))
    
