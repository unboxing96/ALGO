A_list = []
for i in range(10):
    A = int(input())
    A_list.append(A)
print(int(sum(A_list) / len(A_list)))

cnt = []
for j in A_list:
    cnt.append(A_list.count(j))
    if A_list.count(j) == max(cnt):
        result = j
print(result)


