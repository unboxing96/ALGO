# 조건: SEX_UPON_INTAKE Neutered -> O / Spayed -> X로 표시
# 조회: 아이디, 이름, 중성화 여부
# 정렬: 아이디

SELECT 
    animal_id, name, 
    case substring_index(sex_upon_intake, " ", 1)
    when 'Neutered' then 'O'
    when 'Spayed' then 'O'
    when 'intact' then 'X'
    end
    as '중성화'
from 
    animal_ins;
