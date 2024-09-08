# 문제 분석
# 조회: 생물 종, 이름, 성별, 중성화 여부
# 정렬: 아이디
# 조건: 이름이 null인 경우 'no name'

select animal_type, ifnull(name, 'No name') as name, sex_upon_intake
from animal_ins
order by animal_id;