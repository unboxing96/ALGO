# input 값으로 score 리스트 생성
score = []

for i in range(10):
    score.append(int(input())) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


result = 0

for j in score:
    result += j
    if result >= 100: # 계산 결과 100 이상 if문 시작
        if result - 100 > 100 - (result - j): # "계산 이후 - 100" > "100 - 계산 이전"
            result -= j #계산 이후 값이 크다면(100에서 멀다면), 계산 이전 출력
        break # 값이 같다면, 계산 이후 출력

print(result)