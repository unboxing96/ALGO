word = input()

result = ""

for i in word:
    if i not in "CAMBRIDGE":
        result += i

print(result)
