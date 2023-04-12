x, y, w, h = map(int, input().split())
result = min(x, y, abs(w-x), abs(h-y))
print(result)