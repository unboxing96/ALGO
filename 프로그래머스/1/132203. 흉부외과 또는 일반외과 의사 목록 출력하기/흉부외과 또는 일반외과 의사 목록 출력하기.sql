# 진료과가 cs, gs
# 이름, id, 진료과, 고용일자
# 고용일자 내림차순, 이름 오름차순

-- 코드를 입력하세요
select dr_name, dr_id, mcdp_cd, date_format(hire_ymd, '%Y-%m-%d') as hire_ymd
from doctor
where mcdp_cd in ('cs', 'gs')
order by hire_ymd desc, dr_name asc;