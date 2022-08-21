N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))


N_dic = {}
for num in N_list:
    if N_dic.get(num, 0):
        N_dic[num] += 1
    else:
        N_dic[num] = 1

for num in M_list:
    if N_dic.get(num, 0):
        print(N_dic[num], end=" ")
    else:
        print(0, end=" ")