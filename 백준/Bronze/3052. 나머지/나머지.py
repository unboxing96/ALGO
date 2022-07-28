ans = []
for i in range(10):
    a = int(input())
    ans.append(a%42)

print(len(set(ans)))