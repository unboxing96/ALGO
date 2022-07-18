# 19.
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# **양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**

# 10의 자리수로 풀어야 할 듯, 거듭제곱 나머지

num = int(input)

cnt = 0

while True:
    if num % (10 ** cnt) == num: break
    cnt += 1

print(cnt)