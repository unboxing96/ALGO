# REST_INFO와 REST_REVIEW 테이블에서 
# 서울에 위치한 식당들의 
# 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문을 작성해주세요. 
# 이때 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고 
# 결과는 평균점수를 기준으로 내림차순 정렬해주시고, 
# 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬해주세요.

# 식당 정보를 기준으로 LEFT JOIN 리뷰 정보
# GROUP BY 식당 정보 AVG(REVIEW_SCORE)

SELECT 
    I.REST_ID,
    REST_NAME,
    FOOD_TYPE,
    FAVORITES,
    ADDRESS,
    ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM 
    REST_REVIEW AS R
    LEFT JOIN REST_INFO AS I
    ON I.REST_ID = R.REST_ID
GROUP BY
    REST_ID
HAVING
    I.ADDRESS LIKE '서울%'
ORDER BY
    SCORE DESC,
    FAVORITES DESC;
    