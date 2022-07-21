# 정수 N을 받는다
T = int(input())
# 1부터 T까지 반복한다
for numbers in range(1, T+1): #1, 2, 3, 4, ...
    # str(num)을 반복한다.
    cnt = 0
    for num in str(numbers): #"1", "2", ... "13"
        # str(num) 반복문의 요소가 in "369"하면 cnt += 1
        if num in "369":
            cnt += 1
    if cnt:
        # True: "-" * cnt 출력
        print("-" * cnt, end=" ")
    else:
        # False: 요소 출력
        print(numbers, end=" ")