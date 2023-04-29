
def 회문인지(word,left,right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def 어떤회문인지(word,left,right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = 회문인지(word,left+1,right)
            check2 = 회문인지(word,left,right-1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0

n = int(input())
for _ in range(n):
    word = input()

    left=0
    right=len(word)-1

    ans = 어떤회문인지(word,left,right)
    print(ans)
