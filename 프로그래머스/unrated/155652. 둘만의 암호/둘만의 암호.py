def solution(s, skip, index):
    result = []

    for ch in s:
        cur_index = 0  # 실제로 이동한 만큼의 카운트
        while cur_index < index:
            ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))  # 다음 알파벳으로 이동
            if ch not in skip:  # skip에 있는 알파벳으로 이동하지 않았으면 카운트 증가
                cur_index += 1
        result.append(ch)  # 결과 문자열에 추가

    return "".join(result)
