for tc in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    tot = 0

    for i in range(2, len(arr) - 2):
        cur_stick = arr[i]
        tmp_cnt = 0
        for cur_top in range(cur_stick, 0, -1):
            for idx in (i-2, i-1, i+1, i+2):
                if cur_top <= arr[idx]:
                    break
            else:
                tmp_cnt += 1 # 현재 막대의 현재 높이에 대해 성공

        tot += tmp_cnt

    print(f"#{tc + 1} {tot}")
