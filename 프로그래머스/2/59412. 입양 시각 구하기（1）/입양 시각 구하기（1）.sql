# 조건: 09:00 ~ 19:59까지 각 시간대별로 입양이 몇 건 발생했는지?
# 정렬: 시간대 순서로

SELECT DATE_FORMAT(datetime, '%k') AS hour, COUNT(*) AS COUNT
FROM animal_outs
WHERE TIME(datetime) BETWEEN '09:00:00' AND '19:59:00'
GROUP BY hour
ORDER BY hour + 0;
