# 문제 분석
# 조회: 몇 명인지
# 조건: 2021년 가입, 나이 20세 이상 29이하

SELECT count(*)
from user_info
where joined like ('2021%') and age between 20 and 29;