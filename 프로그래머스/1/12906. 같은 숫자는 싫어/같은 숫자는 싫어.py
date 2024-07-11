# 문제 분석
# 배열의 순서를 유지하며, 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

# 접근
# 스택
# 스택의 top이 현재 원소와 같으면 추가하지 않는다.
# 나머지의 경우에는 추가한다.
# 스택을 정순으로 출력한다.

def solution(arr):
    answer = []
    
    for elem in arr:
        if not answer or answer[-1] != elem:
            answer.append(elem)

    return answer