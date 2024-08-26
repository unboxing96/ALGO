n = int(input())
a = n
arr = []
b = 2
while True:
    if a == 1:
        break
    if a % b  == 0 :
        arr.append(b)
        a /= b
        b = 2
    else:
        b +=1

for i in arr:
    print(i)