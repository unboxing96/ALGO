def rule(n1, n2, cnt):
    global max_cnt, max_path

    if n1 - n2 < 0:  # 종료 조건: 음수가 되면 종료
        tmp_path.append(n1)
        tmp_path.append(n2)  # 마지막 원소 추가
        if cnt + 1 > max_cnt:  # 최대 카운트 및 경로 갱신
            max_cnt = cnt + 1
            max_path = tmp_path[:]
        return

    tmp_path.append(n1)
    rule(n2, n1 - n2, cnt + 1)

n = int(input())
max_cnt = 0
max_path = []

for candi in range(n // 2, n + 1):
    tmp_path = []
    rule(n, candi, 1)

print(max_cnt)
print(*max_path)
