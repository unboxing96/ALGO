def jjak(num):
    jj = list(map(int, str(num))) # 돌고 있는 숫자 분해 후 리스트
    jj_result = 0
    for i in jj:
        if (i == 3) or (i == 6) or (i == 9):
            jj_result += 1
    
    return jj_result

T = int(input())
result = []

for num in range(1, T+1):

    if jjak(num):
        result.append("-" * jjak(num))  
    else:
        result.append(num)

for k in result:
    print(k, end=" ")