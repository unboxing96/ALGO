# 문자열을 순회하며 타입을 기준으로 나눔
# 문자열 리스트, 숫자 리스트에 각각 추가
# 문리 정렬
# 숫리 더함
# 문리 + 숫리합 출력

data = input()

result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

result.append(str(value))

print("".join(result))