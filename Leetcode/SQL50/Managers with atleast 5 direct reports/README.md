### Understand the Question
1. #### What is the meaning of manager id in this problem ?
    ##### A direct report is an employee whose manager_id = manager's id
    ##### Example for John number of direct reports are 5. Dan, James, Amy, Anne, Ron.
    ##### We have to find managers who have atleast 5 direct reports. Hence John will be the output
  
# Things learnt from this Question
1. WHERE always comes before ORDER BY
2. COUNT function cannot be used if you have not used GROUP BY

SELECT name
FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5;

##### This query is incorrect because using this query the system will group the table based on manager id but it doesnt know what select name means. which name 
##### to return as output

## Final Answer
SELECT Employee.name \
FROM   \
    (SELECT managerId  \
        FROM Employee   \
        GROUP BY managerId   \
        HAVING COUNT(managerId) >= 5  \
)s INNER JOIN Employee   \
WHERE id = s.managerId

#### 
