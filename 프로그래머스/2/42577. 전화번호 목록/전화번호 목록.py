# 이해
# 어떤 번호가 다른 번호의 접두어인 경우 false
# 아니라면 true
# str.startswith() / str.endswith() -> Bool

# 풀이
# phone_book을 탐색하며, 딕셔너리에서 현재 단어가 없다면,
# 현재 단어를 1글자씩 tmp에 더해가며 딕셔너리가 True가 반환되는 것이 있는지 확인.
# 있으면 return 없으면 완성된 단어를 True로 갱신


def solution(phone_book):
    phone_book.sort()
    dic = {}
    
    for pb in phone_book:
        if pb in dic:  # 'try' 대신 'if'를 사용하여 사전에 키가 존재하는지 확인
            return False
        
        tmp = ""
        for pb_chr in pb:
            tmp += pb_chr
            if tmp in dic:  # 여기서도 동일하게 'if' 사용
                return False
                
        dic[pb] = True  # 단어를 사전에 추가
    
    return True
