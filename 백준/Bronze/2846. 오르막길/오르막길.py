N = int(input()) 
Pi = list(map(int, input().split()))

# 높이 값
val = 0

# 높이 값 모음
result = []

# for문으로 list를 돌며
for i in range(N-1):
    # 다음 수가 더 크면, 다음 수의 인덱스부터 오르막길 리스트(val)에 값 추가 
    if Pi[i] < Pi[i+1]:
        val += Pi[i+1] - Pi[i]
    else:
        # # 0보다 작으면 결과 리스트에 저장. 
        result.append(val)
        # 오르막길 리스트 초기화.
        val = 0
# 반복문 끝나면 결과 리스트 저장
result.append(val)

# 결과 리스트 중 max() 출력
print(max(result))
