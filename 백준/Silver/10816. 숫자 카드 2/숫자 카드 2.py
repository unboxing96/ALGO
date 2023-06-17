from collections import defaultdict

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

cnt_dic = defaultdict(int)

for n_elem in n_list:
    cnt_dic[n_elem] += 1

for m_elem in m_list:
    print(cnt_dic[m_elem], end=" ")