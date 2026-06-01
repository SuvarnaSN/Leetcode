### We have Project table and Employees Table. 
##### Project table has all Project id's and Employee id's. This table answers which employee is working in which project
##### We have Employee table employee_id, name, experience_years. This table tells us how many years of experience does the employee have?

### Question : Average experience years = sum of experience years of employees in that project / number of employees in that project

project_id	employee_id  \
1	          1      \
1	          2      \
1	          3      

##### Employees in project 1 = 1, 2, 3
##### Look for these employees in employee table and then fetch the experience years = 3, 2 , 1 and calculate average now
(3 + 2 + 1) / 3
= 6 / 3
= 2.00

#### So here we can use INNER JOIN because we need every row in project with project_id and we map every employee_id in both 
#### so we can get the years of experience from the second table only that matches with the first table.

After INNER JOIN:
project_id	employee_id	experience_years
1	1	3
1	2	2
2	4	2



