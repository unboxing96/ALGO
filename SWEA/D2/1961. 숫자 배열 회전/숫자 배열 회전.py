# 문제 분석
# 배열을 90도, 180도, 270도 회전한 배열을 출력
# 출력할 때 형식이 특이하다. arr90, arr180, arr270을 생성하고 출력을 한 번에 하자.

# 회전 분석
    # 기본
        # 00 01 02
        # 10 11 12
        # 20 21 22
    # 90도: x 위치에 j를 역순으로 {} / y 위치에 i를 정순으로 {}: arr90[i][j] = arr[N - j + 1][i]
        # 20 10 00 
        # 21 11 01
        # 22 12 02

def rotate90(n, startArr, targetArr):
    for i in range(n):
        for j in range(n):
            targetArr[i][j] = startArr[n - j - 1][i]

    return targetArr

testCase = int(input())
for tc in range(testCase):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    arr90 = [[0 for _ in range(n)] for _ in range(n)]
    arr180 = [[0 for _ in range(n)] for _ in range(n)]
    arr270 = [[0 for _ in range(n)] for _ in range(n)]

    arr90 = rotate90(n, arr, arr90)
    arr180 = rotate90(n, arr90, arr180)
    arr270 = rotate90(n, arr180, arr270)

    print(f"#{tc + 1}")
    for i in range(n):
        result90 = "".join(map(str, arr90[i]))
        result180 = "".join(map(str, arr180[i]))
        result270 = "".join(map(str, arr270[i]))
        result = f"{result90} {result180} {result270}"
        print(result)
