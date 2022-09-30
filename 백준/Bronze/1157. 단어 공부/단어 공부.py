from collections import Counter

word = input()
words = word.lower()
result = Counter(words)

answer = []
most = result[max(result, key=result.get)]

for k, v in result.items():
    if v >= most:
        answer.append(k)

if len(answer) > 1:
    print("?")
else:
    print(answer[0].upper())
