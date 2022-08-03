cnt = 0

for i in range(8): # i = 1 ~ 8
    line = list(input().split())
    line = line[0] # line = ".F.F...F"
    for j in range(len(line)):
        if line[j] == "F":
            if (i + j) % 2 == 0:
                cnt += 1

print(cnt)