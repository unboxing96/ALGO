ans = []

data = input()

for i in range(1, len(data) + 1):
    start = 0
    end = i
    for j in range(len(data) - i + 1):
        ans.append(data[start : end])
        start += 1
        end += 1
        
print(len(set(ans)))