We can implement this solution either using SELF JOIN or LAG

## SELF JOIN

SELECT w1.id \
FROM Weather w1 \
JOIN Weather w2 \
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 \
WHERE w1.temperature > w2.temperature;


## LAG
LAG is a Window Function. LAG(temperature) means it will give previous row's temperature.

SELECT id 
FROM (  \
&nbsp; &nbsp;  SELECT id, temperature, recordDate, \
&nbsp;&nbsp;&nbsp;     LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp, \
&nbsp;&nbsp;&nbsp;      LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date   \
&nbsp;&nbsp;    FROM Weather \
) t \
WHERE temperature > prev_temp \
AND DATEDIFF(recordDate, prev_date) = 1;

