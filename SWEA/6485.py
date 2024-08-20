import sys
sys.stdin = open("6485.txt")

T = int(input())

for tc in range(1, T + 1):
    print(f"#{tc}", end = " ")
    n = int(input())
    path_arr = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    stop = [int(input()) for _ in range(p)] # 정답을 얻고자 하는 정류장 번호
    stop_cnt = [0] * (max(stop) + 1) # 각 정류장 별로 카운트 수

    for s, e in path_arr:
        for i in range(s, e + 1):
            stop_cnt[i] += 1
    
    result = []
    for i in range(p): # 각 정류장 개수만큼 탐색
        result.append(stop_cnt[stop[i]])
    
    print(*result)