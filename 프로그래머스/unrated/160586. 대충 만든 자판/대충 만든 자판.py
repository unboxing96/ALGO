from collections import defaultdict

def solution(keymap, targets):
    answer = []
    
    # 키보드를 defaultdict로 만들고, 각 글자를 누르는 데 필요한 횟수를 저장
    key_dict = defaultdict(lambda: float('inf'))  # 아무 키도 누르지 않은 상태를 무한대로 초기화

    for i, km in enumerate(keymap, start=1):
        for j, alphabet in enumerate(km, start=1):
            key_dict[alphabet] = min(key_dict[alphabet], j)

    for target in targets:
        press_count = sum(key_dict[t] if t in key_dict else float('inf') for t in target)
        
        # 문자열을 만드는 데 필요한 키 누름 횟수가 무한대라면 -1을 추가
        if press_count == float('inf'):
            answer.append(-1)
        else:
            answer.append(press_count)
    
    return answer

keymap = ["AA", "AC"]
targets = ["B", "F"]
print(solution(keymap, targets))  # Output: [-1, -1]
