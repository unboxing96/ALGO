# 풀이 2.
for tc in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    tot = 0

    for i in range(2, len(arr) - 2): # indexError 방지하기 위해 없는 값은 탐색 안 함
        cur_height = arr[i] # 현재 탐색 중인 막대
        nearby = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]] # 주변 막대의 길이
        max_nearby = 0
        for i in range(4):
            if max_nearby < nearby[i]:
                max_nearby = nearby[i]
        if cur_height > max_nearby: # 현재 막대가 주변 막대 길이 중 최댓값보다 길다면 그만큼 조망권을 확보한 것
            tot += cur_height - max_nearby # 전체에 차이(조망권을 확보한 높이)만큼 더함

    print(f"#{tc + 1} {tot}")