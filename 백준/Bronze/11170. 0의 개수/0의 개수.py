T = int(input())

for tc in range(T):
    li = ""
    a, b = map(int, input().split())
    for i in range(a, b+1):
        li += str(i)
    
    print(li.count("0"))
