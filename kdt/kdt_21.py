num = int(input())
num2 = num

cnt = 0
while num2:
    num2 //= 10
    cnt += 1

num_list = []

for i in range(cnt-1, -1, -1):
    cal = num // (10 ** i) # cal = 4
    num -= cal * (10 ** i)
    num_list.append(cal)



