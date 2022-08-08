para = input()
text = input()

start = 0
cnt = 0
while True:
    if text in para:
        para = para[para.index(text) + len(text): ]
        cnt += 1
    else:
        break

print(cnt)
