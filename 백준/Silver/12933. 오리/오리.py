
s = input()
size = len(s)
visited = [0] * size
quack = 'quack'
count = 0

if size % 5 != 0:
    print(-1)
    exit()
    
def sol(start):
    global count
    idx = 0
    keep = True
    for i in range(start, size):
        if s[i] == quack[idx] and visited[i] == 0:
            visited[i] = 1
            if quack[idx] == 'k':
                if keep:
                    count += 1
                    keep = False
                idx = 0 # 한 번의 싸이클 내에서 quack 문자를 확인했을 때, 다음 quack을 검사하기 위해 idx = 0로 할당한다.
            else:
                idx += 1

for i in range(size):
    sol(i)

if count == 0 or not all(visited):
    print(-1)
else:
    print(count)