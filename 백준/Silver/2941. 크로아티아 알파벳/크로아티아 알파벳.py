li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 크로아티아 사전

word = input()

for letter in li:
    word = word.replace(letter, "@") #크로아티아 알파벳을 발견하면 @로 교체

print(len(word))