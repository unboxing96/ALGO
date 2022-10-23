import sys

sys.stdin = open("2460.txt", "r")

biggest = 0
tot = 0

for _ in range(10):
    off, on = map(int, input().split())
    tot -= off
    tot += on

    if tot > biggest:
        biggest = tot

print(biggest)
