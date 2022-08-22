resist = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

cnt = 0
result = ""

for i in range(3):
    word = input()
    
    if cnt == 0 or cnt == 1:    
        result += str(resist.index(word))
    else:
        result = int(result)
        result *= 10 ** resist.index(word)
        break

    cnt += 1

print(result)