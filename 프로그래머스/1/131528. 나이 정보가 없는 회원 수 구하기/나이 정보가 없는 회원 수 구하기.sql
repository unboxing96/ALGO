# 문제 분석
# 나이 정보가 없는 회원이 총 몇 명인지 출력
# 컬럼명은 USERS

select count(*) as USERS
from user_info
where age is null;