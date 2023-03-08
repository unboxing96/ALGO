import sys
sys.stdin = open("1806.txt", "r")

# 구간합을 생성
# [5, 6, 9, 14, 24, 31, 35, 44, 46, 54]
# 투포인터로 end 구간까지 - start 구간까지
# s보다 커지면 start 구간을 오른쪽으로 밀면서 최소 길이 갱신
# 끝까지 탐색했는데 s를 넘지 않으면 0 출력

n, s = map(int, input().split())
nums = list(map(int, input().split()))
prefix = nums[0]
ans = 100001
start = 0
end = 0

while True:
    if prefix >= s:
        prefix -= nums[start]
        ans = min(ans, end - start + 1)
        start += 1
    else:
        end += 1
        if end == n:
            break
        prefix += nums[end]

if ans == 100001:
    print(0)
else:
    print(ans)