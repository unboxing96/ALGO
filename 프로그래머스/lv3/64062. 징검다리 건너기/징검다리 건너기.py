def solution(stones, k):

	# 이분 탐색의 두 포인터를 '건넌 사람 수'를 기준으로
    left = 1
    right = max(stones) # 문제에서 주어진 최대값 200000000 설정하면 더 빠름
	
    # 왼쪽 포인터가 오른쪽에 닿을 때까지
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
		
        # 선형 탐색하며, 현재 값에서 mid를 빼주고, 설정한 mid 값이 최적인지 판단
        for stone in stones:
        
        	# 현재값 - mid가 0 이하이면 == 징검다리가 0이 되면
            if stone - mid <= 0:
                cnt += 1
                # 연속된 0의 개수가 k 이상이 되면
                if cnt >= k:
                    break
            else:
                cnt = 0

        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left