#### How to extract month from date column which is like 2018-12-18

(SELECT MONTH(trans_date) FROM Transactions) AS month

#### How to check for conditions within a query without writing a subquery
### Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') as month,   \
country, \
COUNT(*) as trans_count , \
SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count, \
SUM(t.amount) as trans_total_amount, \
SUM(CASE WHEN state = 'approved' THEN t.amount ELSE 0 END) AS approved_total_amount  \
FROM Transactions AS t  \
GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m');

##### This has the CASE WHEN statements which are like it has CASE WHEN <condition> THEN <result if condition is true> ELSE <condition is false> END

SELECT DATE_FORMAT(trans_date, '%Y-%m') as month -> This will extract 2026-06 from 2026-06-01   \
SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count -> condition        \
SUM(t.amount) as trans_total_amount -> calculate total amount  

GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m') -> Group by (year-month) dont include date 
