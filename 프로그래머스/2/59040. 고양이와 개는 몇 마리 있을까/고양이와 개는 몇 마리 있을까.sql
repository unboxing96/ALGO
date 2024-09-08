# 조회: 고양이 / 개 각각 몇 마리
# 조건: 고양이 먼저 조회

SELECT animal_type, count(*) as count
from animal_ins
group by animal_type
order by animal_type;