h = []
for i in range(9):
    h.append(int(input()))

sum_h = sum(h)
h.sort()

for i in range(9):
    for j in range(i+1, 9):
        if sum_h - h[i] - h[j] == 100:
            for k in range(9):
                if k == i or k == j: continue
                else:
                    print(h[k])
            exit()