size = int(input())                         # 4

dist = list(map(int, input().split()))      # 2 3 1
price = list(map(int, input().split()))     # 5 2 4 1

tot = 0

tot += dist[0] * price[0]
min_price = min(price[:-1])

for i in range(1, size - 1):
    if min_price > price[i]:
        min_price = price[i]
    
    tot += dist[i] * min_price

print(tot)