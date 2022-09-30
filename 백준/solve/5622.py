data = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9,
}

letters = input()
result = 0

for letter in letters:
    for x in data:
        if letter in x:
            result += data[x] + 1

print(result)
