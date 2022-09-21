N, M = map(int, input().split())

# 성공 / 실패
isBool = True

for i in range(M):
    # 한 더미씩 입력 받음
    num = int(input())
    num_list = list(map(int, input().split()))
    # 더미 내부 반복
    for j in range(num - 1):
        if num_list[j] < num_list[j+1]:
            isBool = False
            break
    if not isBool:
        break

print("Yes" if isBool else "No")