Here’s a 30-second interview shortcut pattern for almost all:

“first occurrence per group / earliest row per group / minimum year per product” type problems
first year per product
earliest order per customer
first login per user
minimum date per group

## Step 1: Find the key row per group
SELECT group_column, MIN(ordering_column) AS first_value
FROM table
GROUP BY group_column;

## Step 2: JOIN back to the original table
SELECT t.*
FROM table t
JOIN (
    SELECT group_column, MIN(ordering_column) AS first_value
    FROM table
    GROUP BY group_column
) x
ON t.group_column = x.group_column
AND t.ordering_column = x.first_value;

## Understanding
For each group, find the earliest row, and return the full row data.
Each user → first login
Each product → first sale year
Each customer → first order

### Subquery -> For each group we store the minimum value
SELECT group_column, MIN(ordering_column) AS first_value
FROM table
GROUP BY group_column

group_column	first_value
A	2019
B	2020
C	2018

### JOIN this with the original table
JOIN (
    SELECT group_column, MIN(ordering_column) AS first_value
    FROM table
    GROUP BY group_column
) x
ON t.group_column = x.group_column   -> JOIN condition

