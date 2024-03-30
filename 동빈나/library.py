array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
result = []

count = [0] * (max(array) + 1) # 값의 모든 범위를 포함하는 카운터 배열. 0으로 초기화

for i in range(len(array)):
    count[array[i]] += 1 # array 원소의 개수를 센다.

for i in range(len(count)):
    for j in range(count[i]): # 현재 원소가 count된 수만큼 반복해서 추가한다.
        result.append(i)

print(result) 