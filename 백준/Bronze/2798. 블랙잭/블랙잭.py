N, M = map(int, input().split()) # N: 카드 장 수, M: 카드 3장의 합
card_list = list(map(int, input().split())) # [5, 6, 7, 8, 9]


# 3중 반복문
max_total = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if (card_list[i] + card_list[j] + card_list[k] > M):
                continue
            else:
                max_total = max(max_total, card_list[i] + card_list[j] + card_list[k])

print(max_total)
