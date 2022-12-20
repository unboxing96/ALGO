now = 0
most = 0

for tc in range(10):
    off, on = map(int, input().split())
    now -= off
    now += on
    if now > most:
        most = now

print(most)