
def solution(S):
    answer = len(S)
    for block in range(1, len(S) // 2 + 1):

        stack = []
        prev_str = S[:block]
        cnt = 1

        for i in range(block, len(S) + 1, block):
            cur_str = S[i : i + block]

            if prev_str == cur_str: # 기존 값을 만났을 때
                cnt += 1

            elif prev_str != cur_str: # 새로운 값을 넣을 때
                if cnt >= 2:
                    stack.append(str(cnt))
                stack.append(prev_str)

                prev_str = cur_str
                cnt = 1
        else:
            stack.append(S[i:])

        tmp_completed_str = "".join(stack)
        answer = min(answer, len(tmp_completed_str))

    return answer