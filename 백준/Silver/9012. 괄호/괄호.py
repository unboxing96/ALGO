T = int(input())

for i in range(T):
    vps = input()
    
    while "()" in vps:
        vps = vps.replace("()", "")
    
    if vps:
        print("NO")
    else:
        print("YES")