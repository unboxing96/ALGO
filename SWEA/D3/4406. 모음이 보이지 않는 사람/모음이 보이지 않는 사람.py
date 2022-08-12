
vowels = "aeiou"

T = int(input())

for t in range(1, T+1):
    
    result = []
    word = input()

    for i in word:
        if i not in vowels:
            result.append(i)

    print(f"#{t}", end=" ")
    print(*result, sep="")