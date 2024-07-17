# 문제 접근
# 길이별 중복 순열

result = set()
vowels = "AEIOU"

def solution(word):
    for i in range(1, len(vowels) + 1):
        dfs(vowels, i, 0, "")
        
    sorted_result = sorted(result)
    answer = sorted_result.index(word) + 1
    
    return answer

def dfs(vowels, target_length, index, path):
    global result
    
    # 종료 조건
    if target_length == len(path):
        result.add(path)
        return

    for i in range(index, len(vowels)):
        dfs(vowels, target_length, 0, path + vowels[i])