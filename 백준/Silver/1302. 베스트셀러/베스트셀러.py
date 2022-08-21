T = int(input())

dic = {}
for tc in range(T):
    book = input()
    if dic.get(book, 0):
        dic[book] += 1
    else:
        dic[book] = 1

largest = max(dic.values())

big_dic = {}
for k,v in dic.items():
    if v == largest:
        big_dic[k] = v


    

big_dic = sorted(big_dic.keys())

print(big_dic[0])