# 문제 분석
# 조회: 아이디, 이름, 보호 시작일
# 순서: 이름 오름차순
# 순서: 같은 이름에서는, 보호시작일 내림차순

SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;