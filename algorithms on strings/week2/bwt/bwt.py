# python3
import sys

def BWT(text):
    len_text = len(text)
    lis = []
    for i in range(len_text):
        text = text[-1] + text[:-1]
        lis.append(text)
    lis.sort()
    res = ''
    for i in range(len_text):
        res = res + lis[i][-1]
    return res

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))