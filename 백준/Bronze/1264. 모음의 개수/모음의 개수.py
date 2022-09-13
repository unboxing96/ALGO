vowel = "aeiouAEIOU"

while True:

    lines = input()
    if lines == "#": break

    result = []
    for i in lines:
        if i in vowel:
            result.append(i)
            
    print(len(result))
