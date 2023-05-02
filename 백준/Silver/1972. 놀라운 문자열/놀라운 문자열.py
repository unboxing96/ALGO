
while True:
    data = input()
    if data == '*':
        break
        
    check = True

    for i in range(1, len(data)):
        arr = []
        for j in range(len(data)-i):
            arr.append(data[j] + data[j+i])
        for k in range(len(arr)-1):
            if arr[k] in arr[k+1:]:
                check = False
    if check:
        print(f"{data} is surprising.")
    else:
        print(f"{data} is NOT surprising.")