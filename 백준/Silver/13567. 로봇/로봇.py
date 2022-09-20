# M: 정사각형 길이, n: 명령어 개수
M, n = map(int, input().split())

# 시작 좌표
a = 0
b = 0

# 이동 배열
dir_list = ["R", "U", "L", "D"]

# 첫 방향
dir_num = 0

# 명령어 T/F 여부
isBool = True

# TURN 방향을 문제와 반대로 하면 좌표 계산하기 편할 듯
# 명령어 개수만큼 이동
for i in range(n):

    # text: 명령어 종류, num: 수치
    text, num = input().split()
    num = int(num)

    # 방향 전환
    if text == "TURN":
        if num == 0:
            dir_num = (dir_num - 1) % 4
        elif num == 1:
            dir_num = (dir_num + 1) % 4
        # print("dir_list 인덱스: ", dir_num)

    # 이동 함수
    dir = dir_list[dir_num]
    # print("dir 방향: ", dir)

    # 이동
    if text == "MOVE":
        if dir == "R":
            a += num
        elif dir == "U":
            b -= num
        elif dir == "L":
            a -= num
        elif dir == "D":
            b += num

    if a < 0 or a > M or b < 0 or b > M:
        isBool = False
        print(-1)
        break

    # print(f"{i}번째, {a}, {b}")
    # print("=====================")

if isBool:
    print(a, b)