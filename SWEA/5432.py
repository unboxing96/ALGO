import sys
sys.stdin = open("5432.txt")

T = int(input())

for tc in range(1, T + 1):
    woods = input()
    new_woods = woods.replace("()", "R")

    stack = 0
    tot = 0

    for w in new_woods:
        if w == "(":
            stack += 1
        elif w == ")":
            tot += 1
            stack -= 1
        elif w == "R":
            tot += stack
    
    print(f'#{tc} {tot}')