N = int(input())

# 폭탄 매트릭스
bomb_matrix = []
for _ in range(N):
    bomb_matrix.append(input())

# 클릭 매트릭스
click_matrix = []
for _ in range(N):
    click_matrix.append(input())

# 숫자 매트릭스 (출력)
number_matrix = [["."] * N for _ in range(N)]


for i in range(N):
    for j in range(N):
        # 클릭O
        if click_matrix[i][j] == "x":
            # 폭탄 X
            if bomb_matrix[i][j] == ".":
                # 클릭 위치 + 주변 8개 순회, 폭탄 있으면 cnt += 1
                cnt = 0
                for ii in range(i-1, i+2):
                    if ii == -1 or ii == N: continue # indexError 방지
                    for jj in range(j-1, j+2):
                        if jj == -1 or jj == N: continue #indexError 방지
                        if bomb_matrix[ii][jj] == "*":
                            cnt += 1

                # 폭탄 개수만큼 숫자 매트릭스 업데이트, str()로 통일
                number_matrix[i][j] = str(cnt)

            # 폭탄 O
            elif bomb_matrix[i][j] == "*":
                # 폭탄 매트릭스 순회하며, 숫자 매트릭스에 "*" 추가
                for a in range(N):
                    for b in range(N):
                        if bomb_matrix[a][b] == "*":
                            number_matrix[a][b] = "*"

result = []

for i in range(N):
    result.append("".join(number_matrix[i]))

for i in result:
    print(i)