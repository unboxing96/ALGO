T = int(input())

seat = list(map(int, input().split()))

print(len(seat) - len(set(seat)))