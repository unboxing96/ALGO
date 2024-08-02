# 문제 분석
# 펠린드롬
# 큐나 스택으로 해도 되고 .. 문자열 인덱싱으로 해보자
# 양 끝에서 출발하는 인덱스를 두고, length // 2번 탐색하면 된다.
# 홀수 길이일 때 가운데는 중요치 않다.

# TestCase 개수
T = int(input())

# TestCase만큼 반복
for tc in range(1, T + 1):
    word = input()
    s = 0
    e = len(word) - 1
    result = 1
    for i in range(len(word) // 2):
        if word[s] != word[e]:
            result = 0
            break
        s += 1
        e -= 1

    print(f'#{tc} {result}')
