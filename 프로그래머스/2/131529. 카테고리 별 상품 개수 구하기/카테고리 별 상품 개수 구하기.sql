# 문제 분석
# 조회: 카테고리 코드별 상품 개수
# 정렬: 카테고리 코드별 오름차순

SELECT substring(product_code, 1, 2) as category, COUNT(*)
from product
group by category
order by category;