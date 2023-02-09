
def solution(gems):

    answer = []
    dict = {}
    tot = len(set(gems))
    s = 0
    e = 0
    distance = len(gems) + 1

    # while loop: 끝점 옮기기
    while e < len(gems):

        # 딕셔너리에 {보석 : 개수} 추가
        dict[gems[e]] = dict.get(gems[e], 0) + 1

        # 끝점 이동
        e += 1

        # 딕셔너리 길이기 보석 개수와 같다면
        if len(dict) == tot:
            # 다시 while loop: 시작점 옮기기
            while s < e:
                # 현재 위치 보석이 딕셔너리에 있다면 -> 제거
                if dict[gems[s]] > 1:
                    dict[gems[s]] = dict.get(gems[s], 0) - 1
                    s += 1

                # 없다면 -> 시작점과 끝점 길이가 현재 구간보다 짧다면 -> 최소 거리 초기화
                elif distance > e - s:
                    distance = e - s
                    answer = [s + 1, e]
                    break

                # 없다면 -> break
                else:
                    break

    return answer
