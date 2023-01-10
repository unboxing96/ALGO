D = {chr(i): i - 64 for i in range(65, 91)}


def solution(msg):
    result = []
    idx = 27
    start, end = 0, 1
    msg += "0"

    while end < len(msg):
        while msg[start:end] in D:
            end += 1

        # 색인 번호 출력 (기존 사전에 있음)
        result.append(D[msg[start : end - 1]])

        # 새로운 단어 사전 추가
        D[msg[start:end]] = idx
        idx += 1  # 사전 인덱스 1 증가

        # 탐색 좌표 수정
        start, end = end - 1, end

    return result