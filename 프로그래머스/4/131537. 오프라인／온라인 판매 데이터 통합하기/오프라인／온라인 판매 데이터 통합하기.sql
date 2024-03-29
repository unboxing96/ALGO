# 두 개의 테이블을 하나로 합쳐야 하는 문제
# JOIN과 UNION 중에 어떤 것을 선택해야 하는가? 차이에 대해서 알아야겠다
# 현재로서는 UNION으로 하자. JOIN은 특정 컬럼을 기준으로 합치는 것으로 기억한다.

SELECT 
    DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
    PRODUCT_ID, 
    USER_ID, 
    SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'

UNION

SELECT 
    DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
    PRODUCT_ID, 
    NULL AS USER_ID, 
    SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;