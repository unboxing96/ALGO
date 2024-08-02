T = 10
for _ in range(1, T + 1):
    tc = int(input())
    target = input()
    long_string = input()

    target_length = len(target)
    long_string_length = len(long_string)

    cnt = 0
    for i in range(long_string_length - target_length + 1): # +1을 해주어야, 문자열 끝에 붙은 target 하나를 빠뜨리지 않을 수 있다.
        isMatch = True
        for j in range(len(target)):
            if long_string[i + j] != target[j]:
                isMatch = False
                break
        if isMatch:
            cnt += 1

    print(f'#{tc} {cnt}')