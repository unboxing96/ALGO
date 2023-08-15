def solution(lottos, win_nums):
    answer = []

    base = set(lottos) & set(win_nums)
    cnt_zero = lottos.count(0)

    upper_rank = min(6, 7 - (len(base) + cnt_zero))
    lower_rank = min(6, 7 - len(base))

    return [upper_rank, lower_rank]