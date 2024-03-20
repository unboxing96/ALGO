import sys
sys.stdin = open("왕실의나이트.txt", "r")

start_str_idx = input()
start_idx = [ord(start_str_idx[0]) - int(ord("a")) + 1, int(start_str_idx[1])]

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0

for i in range(8):
    nx = start_idx[0] + dx[i]
    ny = start_idx[1] + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    
    count += 1

print(count)
