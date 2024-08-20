import sys
sys.stdin = open("14696.txt")

n = int(input())
for _ in range(n):
    left = []
    right = []
    for i in range(2):
        cnt, *arr = map(int, input().split())
        if i == 0:
            left = arr
        else:
            right = arr
    
    for symbol in range(4, 0, -1):
        ls = left.count(symbol)
        rs = right.count(symbol)

        if ls > rs:
            print('A')
            break
        elif ls < rs:
            print('B')
            break
        else:
            continue
    else:
        print('D')