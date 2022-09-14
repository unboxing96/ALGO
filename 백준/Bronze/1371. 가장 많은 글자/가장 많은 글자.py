import sys

lines = sys.stdin.read()
data = [0] * 26

for line in lines:
    if line.islower():
        data[ord(line) - 97] += 1

for i in range(26):
    if data[i] == max(data):
        print(chr(i + 97), end="")
