# 문제 분석
# 조건: 이름이 null인 동물의 id
# 정렬: id의 오름차순

SELECT animal_id
from animal_ins
where name is null
order by animal_id;