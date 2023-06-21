def solution(n, m, section):

    now = section[0]
    cnt = 1 # 최소 1번 칠하고 시작

    for i in range(1, len(section)):
        if section[i] - now >= m: # 한 번의 색칠로 m-1 길이의 범위만큼 덧칠
            cnt += 1
            now = section[i]

    return cnt
