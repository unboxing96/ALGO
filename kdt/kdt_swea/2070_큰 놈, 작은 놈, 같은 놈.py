import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for i in range(1, T+1):

    a, b= map(int, input().split())

    if a < b:
        print(f"#{i} <", end="\n")
    elif a == b:
        print(f"#{i} =", end="\n")
    else:
        print(f"#{i} >", end="\n") 