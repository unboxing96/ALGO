# 문제 분석
# 조회: 이름이 있는 동물의 ID
# 순서: ID 오름차순

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;