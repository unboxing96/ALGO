# 문제 분석
# 테이블 윗 부분 N극(1), 아래 부분 S극(2)
# 배열의 자성체도 같다. 1은 2에 끌린다. 2는 1에 끌린다.
# 자성체는 1초마다 1칸씩, 반대 극의 방향으로 이동한다.
# 배열을 벗어나면 사라진다.
# 반대 극의 자성체를 만나면 교착 상태에 빠지고 더 이상 움직이지 않는다.
# 더 이상 이동이 발생하지 않을 때, 교착 상태의 개수를 구하라

# 교착 상태 중, 쌍이 번갈아서 나오면 다른 교착 상태로 본다.
# 뭉쳐있으면 하나의 교착 상태로 본다.

# 접근
# 행렬 이동을 직접 구현할 필요는 없는 듯하다.
# 각 배열을 열 방향으로 탐색한다.
# 윗 줄에서 N극(1)이, 아랫 줄에서 S극(2)이 존재하면 교착 상태 += 1을 한다.
# 교착 상태가 완성된 이후에는, 다시 새로운 교착 상태를 찾을 수 있다.
# isNorth, isSouth 변수를 사용해서, 모두 True가 되면 deadlock += 1 하고, idx 이동하고, 각 변수를 다시 False로 변경한다.
# 순서가 중요하다. North가 먼저 True인 상태에서 South가 True가 되어야 += 1이다.
    # North는 그냥 True로 변경할 수 있다.
    # South는 North가 True인 경우에만 True로 변경할 수 있다.

# TestCase 개수
T = 10

# TestCase만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    deadlock = 0

    for j in range(n):
        isNorth = False
        isSouth = False
        for i in range(n):
            if matrix[i][j] == 1:
                isNorth = True
            elif matrix[i][j] == 2 and isNorth:
                # isSouth = True
                deadlock += 1
                isNorth = False
                # isSouth = True

    print(f'#{tc} {deadlock}')