# 문제 분석
# 시작점 n1이 주어진다.
# 다음 지점 n2를 start 이하의 범위에서 선택한다.
# 이후에는 재귀적으로 next = f(n1 - n2)
# next가 음의 정수가 되면, 이 수를 버리고 재귀 함수를 종료한다.
# 이때 만들어지는 수가 가장 큰 경우의 개수와, path를 출력하라.

# 재귀함수를 구현한다.
# N // 2부터 N까지 탐색하며 최댓값을 구한다.

def rule(n1, n2, cnt):
    global max_cnt
    if n1 - n2 < 0: # 종료 조건 # 마지막 원소 추가
        tmp_path.append(n1)
        tmp_path.append(n2)
        return cnt + 1
    
    tmp_path.append(n1)

    return rule(n2, n1 - n2, cnt + 1)

n = int(input())
max_cnt = 0
max_path = []

for candi in range(n // 2, n + 1):
    tmp_path = []
    tmp_cnt = rule(n, candi, 1)
    
    if tmp_cnt > max_cnt:
        max_cnt = tmp_cnt
        max_path = tmp_path[:]

print(max_cnt)
print(*max_path)