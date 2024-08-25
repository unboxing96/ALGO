def binary_search_left(words, query):
    start, end = 0, len(words)
    while start < end:
        mid = (start + end) // 2
        if words[mid] < query:
            start = mid + 1
        else:
            end = mid
    return start

def binary_search_right(words, query):
    start, end = 0, len(words)
    while start < end:
        mid = (start + end) // 2
        if words[mid] <= query:
            start = mid + 1
        else:
            end = mid
    return start

def solution(words, queries):
    answer = []
    word_cnt_arr = [[] for _ in range(10001)]
    reverse_word_cnt_arr = [[] for _ in range(10001)]

    for word in words:
        word_cnt_arr[len(word)].append(word)
        reverse_word_cnt_arr[len(word)].append(word[::-1])
        
    for i in range(10001):
        word_cnt_arr[i].sort()
        reverse_word_cnt_arr[i].sort()
    
    for query in queries:
        query_to_A = query.replace('?', 'a')
        query_to_Z = query.replace('?', 'z')
        
        if query[0] == '?':
            start = binary_search_left(reverse_word_cnt_arr[len(query)], query_to_A[::-1])
            end = binary_search_right(reverse_word_cnt_arr[len(query)], query_to_Z[::-1])
            answer.append(end - start)
        else:
            start = binary_search_left(word_cnt_arr[len(query)], query_to_A)
            end = binary_search_right(word_cnt_arr[len(query)], query_to_Z)
            answer.append(end - start)
    
    return answer
