import sys
sys.stdin = open("1860.txt")

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end = " ")
    n, m, k = map(int, input().split())
    waiting = list(map(int, input().split()))
    waiting.sort()

    for i in range(len(waiting)):
        done = (waiting[i] // m) * k # 손님이 도착한 순간 만들어져있는 개수
        if done < i + 1: # i번째 사람이 왔을 때 i개보다 적으면 불가
            print("Impossible")
            break
    else:
        print("Possible")