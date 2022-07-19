import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    quotient = a // b
    remainder = a % b
    print(f"#{i+1}", quotient, remainder, end = "\n")