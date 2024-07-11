# 문제 분석
# 숫자문자열로 구성된 배열
# 배열의 어떠한 요소가 다른 요소의 접두사가 된다면 false 아니면 true
# 배열의 길이가 1,000,000이므로 O(N ** 2)은 곤란하다.

# 접근
# phone_book을 탐색하며 각 요소를 모두 해시맵에 넣자
# phone_book을 다시 탐색하며, 각 요소를 중첩 탐색한다.
    # 요소를 한 글자씩 더해가며 해시맵에 있는지 판단한다.
    # 해시맵에 있더라도, 두 개의 요소가 정확히 같으면 pass 해야 한다.

def solution(phone_book):
    hashMap = {}
    
    for phoneNum in phone_book:
        hashMap[phoneNum] = True
    
    for phoneNum in phone_book:
        temp = ""
        for num in phoneNum:
            temp += num
            
            if hashMap.get(temp, 0) and temp != phoneNum:
                return False
    return True