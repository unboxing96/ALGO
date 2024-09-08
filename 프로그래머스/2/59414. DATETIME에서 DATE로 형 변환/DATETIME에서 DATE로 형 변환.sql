# 문제 분석
# 조회: 아이디, 이름, 들어온 날짜(형식)
# 정렬: 아이디

SELECT animal_id, name, date_format(DATETIME, '%Y-%m-%d') as '날짜'
from animal_ins
order by animal_id;