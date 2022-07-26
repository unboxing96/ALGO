sum_list = []
for i in range(5):
    a = list(map(int, input().split()))
    sum_list.append(sum(a))

print(sum_list.index(max(sum_list))+1, max(sum_list))