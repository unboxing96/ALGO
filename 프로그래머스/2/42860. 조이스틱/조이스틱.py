# 이해
# while True
# 현재 위치가 A가 아니라면, 유니코드상 A와의 차이만큼 result에 더해준다.
# min(현재 위치 - array.index("A")의 위치, name 길이 - array.index("A") + 현재 위치)만큼 result에 더한다.
# 포인터를 array.index("A")로 옮긴다.

def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord("A"), ord("Z")-ord(char) + 1) # 문자 변경 비용
        
        next = i + 1
        while next < n and name[next] == "A":
            next += 1
        
        distance = min(i, n - next)
        min_move = min(min_move, i + n - next + distance)
    
    answer += min_move
    return answer
