T = int(input())

dic = {}
for tc in range(T):
    name, TF = input().split()
    if TF == "enter":
        dic[name] = TF
    else:
        del dic[name]

dic = sorted(dic.keys(), reverse=True)

for i in dic:
    print(i)