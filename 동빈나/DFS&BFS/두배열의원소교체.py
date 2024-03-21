import sys
sys.stdin = open("두배열의원소교체.txt", "r")

# 바꿔치기 k번으로 첫 번째 배열의 합을 최대로
# 양쪽 배열을 정렬해서, 왼쪽에서는 작은 것 순서대로, 오른쪽에서는 큰 것 순서대로 바꾸기
# 이떄, 왼쪽 원소가 작을 때에만 교체

n, k = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

first_arr.sort()
second_arr.sort(reverse=True)

for i in range(k):
    if first_arr[i] < second_arr[i]:
        first_arr[i], second_arr[i] = second_arr[i], first_arr[i]
    else:
        break # 더 이상 교환이 필요한 경우가 없다.

print(sum(first_arr))