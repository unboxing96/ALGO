import sys

sys.stdin = open("1062.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
elif k == 25:
    print(n)
    exit()

ans = 0
dic = [0] * 26
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]

print(words)

# 필수 단어 만들기
for i in "acint":
    dic[ord(i) - ord("a")] = 1
