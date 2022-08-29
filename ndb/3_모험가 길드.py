# 공포도 = 그룹에 필요한 사람 수
# 여행을 떠날 수 있는 그룹 수의 최댓값

# 오름차순 정렬
# 그룹원 수 = 팀 내 최대 공포도 일치하면 바로 출발


result = 0
cnt = 0

N = int(input())
list_ = list(map(int, input().split()))

list_.sort()

for i in list_:
    
    cnt += 1

    if cnt >= i:
        result += 1
        cnt = 0

print(result)