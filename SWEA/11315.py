import sys
sys.stdin = open("11315.txt")


TC = int(input())
for tc in range(1, TC + 1):

    def solution():
        n = int(input())
        matrix = [input() for _ in range(n)]
        dx = [1, 1, 1, 0]
        dy = [-1, 0, 1, -1]

        for x in range(n):
            for y in range(n):
                if matrix[x][y] == 'o':
                    for i in range(4):
                        tmp_cnt = 1
                        nx = x + dx[i]
                        ny = y + dy[i]

                        while 0 <= nx < n and 0 <= ny < n:
                            if matrix[nx][ny] != 'o':
                                break
                            tmp_cnt += 1
                            nx += dx[i]
                            ny += dy[i]
                        
                        if tmp_cnt == 5:
                            return "YES"
        
        return "NO"
    
    result = solution()
    print(f"#{tc} {result}")