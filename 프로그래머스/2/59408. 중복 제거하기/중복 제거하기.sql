# 문제 분석
# 조회: 동물의 이름이 몇 개?
# 조건: 이름 IS NOT NULL / 중복 없이

SELECT COUNT(DISTINCT NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;