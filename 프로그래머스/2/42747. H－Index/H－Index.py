# 이해
# 주어진 배열을 h를 기준으로 둘로 나눈다.
# 이때 h 이상인 배열의 길이가 h 이상이 된다. h 이하인 배열의 길이가 h 이하가 된다. 이것이 h-index.
# 이분탐색처럼 느껴지기도 한다.
# 그러나 n의 크기가 1000 이하 이므로 O(N ** 2)으로 완전탐색해도 되겠다.

# 풀이
# 배열을 정렬한다.
# 피봇 h를 정한다. 대략 길이의 절반쯤 위치의 인덱스로
# 피봇을 기준으로 큰 값과 작은 값을 계산한다.
# 피봇을 적당히 옮겨서 h의 최댓값을 구한다.

def solution(citations):
    citations.sort()
    n = len(citations)
    h_index = 0
    
    for i, citation in enumerate(citations):
        h = min(citation, n - i)  # 피봇값 계산
        h_index = max(h_index, h)  # h-index 갱신
    
    return h_index
