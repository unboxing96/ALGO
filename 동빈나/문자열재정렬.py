import sys
sys.stdin = open("문자열재정렬.txt", "r")

# 문자 배열, 숫자 배열 분리

string = input()
str_arr = []
int_arr = []

for s in string:
    if s.isalpha():
        str_arr.append(s)
    else:
        int_arr.append(int(s))

str_arr.sort()
print("".join(str_arr) + str(sum(int_arr)))