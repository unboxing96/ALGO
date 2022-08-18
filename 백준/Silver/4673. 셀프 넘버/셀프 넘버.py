origin_num = list(range(1, 10001))
generated_num = []

for num in origin_num:
    for i in str(num):
        num += int(i)
    generated_num.append(num)

for i in origin_num:
    if i not in generated_num:
        print(i)