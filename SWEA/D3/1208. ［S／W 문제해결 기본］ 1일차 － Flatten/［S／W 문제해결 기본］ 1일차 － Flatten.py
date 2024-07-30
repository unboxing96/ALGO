#1.

# 문제 분석
# 평탄화 한다.
# 더 이상 평탄화 할 수 없으면, 입력값에 따라 0 혹은 1을 출력
# 평탄화 횟수에는 제한이 있다.

# 접근
# 가로 길이가 100이므로 완전 탐색해도 풀이할 수 있다.
# 카운트 배열을 생성한다.
# 주어진 횟수만큼 반복한다.
    # 아래에서 가장 큰 인덱스와 가장 작은 인덱스는 0이면 안 된다. 값이 있어야 한다.
    # 가장 큰 값을 갖고 있는 인덱스 (끝 인덱스) -= 1
    # 가장 작은 값을 갖고 있는 인덱스 -= 1
    # 그 다음 작은 값을 갖고 있는 인덱스 += 1
    
# TestCase 개수
T = 10

def my_max(iterable):
    max_num = iterable[0]
    for i in range(1, len(iterable)):
        if max_num < iterable[i]:
            max_num = iterable[i]
    return max_num

# TestCase만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    counts = [0] * (my_max(arr) + 1)
    for i in range(len(arr)):
        counts[arr[i]] += 1

    s = 0
    e = len(counts) - 1
    cnt = 0
    while s + 1 < e and cnt < n:
        if not counts[e]:
            e -= 1
            continue
        if not counts[s]:
            s += 1
            continue

        counts[e] -= 1
        counts[s] -= 1
        counts[s + 1] += 1
        counts[e - 1] += 1
        cnt += 1

    while counts[s] == 0: # 탐색 끝낸 뒤에, 가장 낮은 높이
        s += 1

    while counts[e] == 0: # 탐색 끝낸 뒤에, 가장 높은 높이
        e -= 1

    print(f'#{tc} {e - s}')