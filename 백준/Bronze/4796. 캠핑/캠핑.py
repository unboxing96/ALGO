import sys
input = sys.stdin.readline

i = 1
while True:
    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break
        
    res = (v//p)*l
    res += min((v%p), l)
    print('Case %d: %d' %(i, res))
    i += 1