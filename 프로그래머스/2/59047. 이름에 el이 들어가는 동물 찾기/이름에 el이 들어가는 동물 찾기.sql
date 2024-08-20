# 문제 분석
# 이름에 "EL"이 들어가는 개의 / 아이디와 이름을 조회
# 이름 순 조회
# 이름의 대소문자 구분하지 않음

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'DOG'
ORDER BY NAME;