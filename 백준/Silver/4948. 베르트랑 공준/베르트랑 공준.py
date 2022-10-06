def getPrimaryNum_Eratos(N):
    nums = [True] * (N)
    for i in range(2, int(N**0.5) + 1):
        if nums[i] == True:
            for j in range(i+i ,N, i):
                nums[j] = False
    return [i for i in range(2, N) if nums[i] == True]

while True:
    N = int(input())
    
    if N == 0:
        break
    prime_list = getPrimaryNum_Eratos(2*N + 1)
    answer_list = [num for num in prime_list if num > N]
    print(len(answer_list))