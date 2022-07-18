# 13. 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# word = "apple"

# # 빈 리스트(new_word_list) 생성. word의 뒤에서부터 인덱싱하여, 빈 리스트에 추가
# new_word_list = []

# for i in range(1, len(word) + 1):
#     new_word_list.append(word[-i])

# # for문. 차례대로 str(result)에 더함
# result = ""

# for j in new_word_list:
#     result += j

# print(result)


#####훨씬 간단한 풀이#####

# word = "apple"

# new_word_list = ""

# for i in word:
#     new_word_list = i + new_word_list

# print(new_word_list)
# print(new_word_list[::-1])



### 더 좋은 풀이 ###

word = "apple"

for i in range(len(word)):
    print(word[-i-1], end="")