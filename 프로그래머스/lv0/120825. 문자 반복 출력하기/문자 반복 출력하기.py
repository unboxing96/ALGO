def solution(my_string, n):
    text = []
    for word in my_string:
        for _ in range(n):
            text.append(word)
    answer = "".join(text)
    return answer