n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 나머지가 같은 원소 저장하는 배열
remainder = [0 for _ in range(m)]
remainder[0] = 1 # 누적합의 첫 번째 항은 0이므로 나머지가 0인 원소라고 치고 += 1

tot = 0
for i in range(n):
    tot += nums[i] # 누적합
    r = tot % m # 나머지
    remainder[r] += 1 # 현재 누적합을 m으로 나눈 나머지에 += 1

# 나머지에 따라 나뉜 누적합 구간들 -> 같은 나머지에서 2개 뽑는 조합
cnt = 0
for size in remainder:
    cnt += size * (size - 1) // 2

print(cnt)