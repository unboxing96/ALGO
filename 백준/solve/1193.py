x = int(input())

row = 0
idx = 0
while x > idx:
    row += 1
    idx += row

diff = idx - x

if row % 2 == 0:
    top = row - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = row - diff

print(f"{top}/{bottom}")
