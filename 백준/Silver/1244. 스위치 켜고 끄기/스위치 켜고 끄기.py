n = int(input())
switch = list(map(int, input().split()))
tc = int(input())

for _ in range(tc):
    gender, idx = map(int, input().split()) # 실제 위치는 idx - 1

    if gender == 1: # 남자
        for i in range(n):
            if (i + 1) % idx == 0:
                switch[i] = 1 - switch[i]
    
    elif gender == 2: # 여자
        idx -= 1
        switch[idx] = 1 - switch[idx] # 현재 위치 뒤집기
        k = 1
        while idx - k >= 0 and idx + k < n and switch[idx - k] == switch[idx + k]:
            switch[idx - k] = 1 - switch[idx - k]
            switch[idx + k] = 1 - switch[idx + k]
            k += 1

for i in range(0, len(switch), 20):
    print(*switch[i : i + 20])