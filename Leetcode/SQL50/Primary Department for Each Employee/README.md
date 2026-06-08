#### Each row in the output table says one employee belongs to one department or multiple rows per employee
#### Many rows -> one result per employee

#### We are not clubbing everything together or aggregating anything we are just getting one row per employee_id . So we just need to do GROUP BY employee_id
#### Which department should represent each employee -> Prefer employee_id with primary_flag = 'Y'. If not fallback to any dept -> This is a priority selection problem.

#### How to pick best row per group
Problem type	Tool   \
pick max/min      ->	MAX / MIN \
conditional pick  ->	CASE WHEN   \
fallback logic	  ->  COALESCE    \
ranking rows	    ->  ROW_NUMBER()  

“CASE runs per row → then GROUP BY aggregates those results”

## COALESCE(
##    MAX(CASE WHEN primary_flag = 'Y' THEN department_id END),
##    MAX(department_id)
## ) AS department_id

#### Try to get the primary department first if not fallback to any department
#### For each row if primary flag is Y returns department_if else null. So same thing will happen for every row. Then the results are grouped together by MAX for every employee.
#### Fall back -> Fall back means if there is no row with any primary_flag = 'Y' then it will return MAX(department_id) as a fallback value
#### COALESCE(primary_value, fall_back value)  -> This will print the non null value. If primary = NULL print fallback value else print primary value

#### Case 1: primary exists => COALESCE(10, 30) → 10
#### Case 2: primary missing => COALESCE(NULL, 30) → 30
