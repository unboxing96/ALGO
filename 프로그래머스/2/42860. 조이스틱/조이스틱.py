# 이해
# A로만 이루어진 문자열을 움직여서 name을 완성하고, 완성하기까지 조작 횟수의 최솟값을 return
# 조작은 위치를 이동하는 조작과, 문자열을 바꾸는 조작이 있다.
# 모든 조작은 한 쪽 끝에서 반대 방향으로 조작하면, 반대편 끝으로 이동한다.
# 이동: 순차적으로 탐색하는 것과, 왼쪽 끝 시작 위치에서 오른쪽으로 하나씩 이동하다가 가장 긴 A를 만나면 돌아가는 것 사이의 최솟값을 구한다.
    # 가장 긴 연속하는 A의 길이가, name 길이의 절반 이상이라면 건너지 않는 것이 좋다.
# 문자열 변경: min(순차 이동, Z부터 역으로 이동 + 1)

# 풀이
# longestA = 가장 긴 연속하는 A의 길이를 구한다.
# longestA >= len(name) // 2 이라면, 
    # longestA를 만나기 전까지 이동한 뒤에, 돌아가는 것이 낫다.
    # 아니라면, 선형 탐색하는 것이 낫다.
# 선형 탐색하면서 문자열 바꾸는 데 소요되는 문자열 조작 횟수를 합산한다.
# 선형 탐색과 longestA를 기준으로 유턴하는 이동 조작 횟수 중 최소를 합산한다.

def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        
        min_move = min(min_move, 2 * i + (len(name) - next), i + (len(name) - next) * 2)
    
    answer += min_move
    return answer
    
    



