# TestCase 개수
T = 10

# TestCase만큼 반복
for _ in range(1, T + 1):
    tc = int(input())
    target = input()
    long_string = input()

    cnt = 0
    idx = 0
    target_length = len(target)

    while idx <= len(long_string) - target_length:
        candidate_index = long_string[idx:].find(target)
        if candidate_index != -1:
            cnt += 1
            idx += candidate_index + target_length
        else:
            break

    print(f"#{tc} {cnt}")