import sys
sys.stdin = open("16935.txt", "r")

"""
1. 상하 -> 그래프 역순 탐색
2. 좌우 -> 그래프의 각 행을 역순으로 정렬
3. 오른쪽 90도 -> zip()
4. 왼쪽 90도 -> 그래프의 각 행을 역순으로 zip()
5. 시계방향 사분면 ->
6. 반시계방향 사분면
"""

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    oper = int(input())

