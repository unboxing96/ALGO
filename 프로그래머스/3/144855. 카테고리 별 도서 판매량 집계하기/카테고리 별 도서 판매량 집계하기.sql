select b.CATEGORY, SUM(bs.SALES) AS TOTAL_SALES
from book b
join book_sales bs
on b.BOOK_ID = bs.BOOK_ID
where bs.SALES_DATE LIKE "2022-01%"
GROUP BY b.CATEGORY
ORDER BY b.CATEGORY