string = input()

tot = 0
new_integer = -1

for s in string:
    tot += int(s)

if tot % 3 == 0 and "0" in string:
    new_integer = int("".join(sorted(list(string), reverse=True)))

print(new_integer)