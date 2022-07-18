# 12. 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.


word = "apple"

# for문. 비교 연산자로 "a"만 빼고 append
word_list = []

for i in word:
    if i != "a":
        word_list.append(i)
    else: continue

# for문으로 list -> str
result = ""

for j in word_list:
    result += j

print(result)