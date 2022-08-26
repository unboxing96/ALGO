T = int(input())

for tc in range(T):
    car = int(input())
    tool = int(input())
    for i in range(tool):
        a, b = map(int, input().split())
        car += a * b
    print(car)