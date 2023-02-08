n = int(input())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

room.sort(key=lambda x : [x[1], x[0]])

cnt = 1
end_time = room[0][1]
for i in range(1, n):
    if room[i][0] >= end_time:
        cnt += 1
        end_time = room[i][1]

print(cnt)