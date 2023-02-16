def solution(stones, k):
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        flag = False
        
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                flag = True
                break
        
        if flag:
            right = mid - 1
        else:
            left = mid + 1
    
    return left
