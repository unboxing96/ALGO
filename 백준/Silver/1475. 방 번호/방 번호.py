n = int(input())
dic = {str(i) : 0 for i in range(10)}

nums = str(n).replace("6", "9")

for num in nums:
    dic[num] += 1

sorted_dic = sorted(dic.items(), key=lambda x : -x[1])

if sorted_dic[0][0] == "9":
    print(sorted_dic[0][1] // 2 + sorted_dic[0][1] % 2)
else:
    print(sorted_dic[0][1])