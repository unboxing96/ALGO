from collections import Counter


def solution(s):
    answer = []
    word = s.replace("{", "").replace("}", "").split(",")
    count_word = Counter(word)
    print(count_word)
    for i in count_word:
        answer.append(int(i[0]))
    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
