
N, X = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 그래프 만들기
for i in range(1, N):
    arr[i] += arr[i-1]

# 최대 방문자 수 0명이면 SAD 출력
if arr[X-1] == 0:
    print("SAD")
else:
    # 둘째 줄에 기간이 몇 개 있는지 출력
    max_visitor = arr[X-1]
    max_visitor_cnt = 1
    for i in range(X, N):
        if arr[i] - arr[i-X] > max_visitor:
            max_visitor = arr[i] - arr[i-X]
            max_visitor_cnt = 1
        elif arr[i] - arr[i-X] == max_visitor:
            max_visitor_cnt += 1
    print(max_visitor)
    print(max_visitor_cnt)