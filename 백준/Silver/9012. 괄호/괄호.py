t = int(input())

for _ in range(t):
    data = input()

    while "()" in data:
        data = data.replace("()", "")
    
    if not data:
        print("YES")
    else:
        print("NO")