
n, m = map(int, input().split())

dic_name = {}
dic_num = {}

cnt = 1
for _ in range(n):
    data = input()
    if not dic_name.get(data):
        dic_name[data] = cnt
        dic_num[cnt] = data
        cnt += 1

for _ in range(m):
    data = input()
    if data.isdigit():
        print(dic_num[int(data)])
    else:
        print(dic_name[data])