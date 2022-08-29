# 문자열을 받아서
# 왼쪽부터 순회하며
# 곱하기나 더하기 연산하여, 최대값 출력

# 반복값이 0일 떄만 더하고, 나머진 모두 곱하기



number = input()
result = int(number[0])

for i in range(len(number)):

    num = int(number[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)