def frog(word):

    new = []

    for letter in word:

        if 97 <= ord(letter) <= 122:
            new.append(chr(219 - ord(letter)))

        elif 65 <= ord(letter) <= 90:
            new.append(chr(155 - ord(letter)))

        elif ord(letter) == 32:
            new.append(chr(32))

    return "".join(new)


word = "I love you"
result = frog(word)

print(result)
