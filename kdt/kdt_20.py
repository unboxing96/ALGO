# 20.
# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

num = int(input())

num_list = list(map(int, list(str(num))))
print(sum(num_list))



