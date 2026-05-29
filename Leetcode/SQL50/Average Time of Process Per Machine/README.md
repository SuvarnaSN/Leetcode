# Step 1: Understand the Table

Example data: \
<img width="862" height="260" alt="image" src="https://github.com/user-attachments/assets/42331598-9987-4474-b50d-d5ad1963bb3b" />

# Step 2: Process Completion Time

For each process \
completion_time = (end_time - start_time)  \ 
Process1: 1.520 - 0.712 = 0.808  \
Process2: 4.120 - 3.140 = 0.980    \

# Step 3: Average Per Machine
(0.808 + 0.980) / 2


# PARTITION BY 
This is used in window functions like LAG, LEAD, ROW_NUMBER, RANK. We split the data into groups and perform the window function separately inside each group
So when we say

LAG(timestamp) OVER ( \
    PARTITION BY machine_id, process_id \
    ORDER BY timestamp \
)

For each machine, process combination, look at the previous timestamp.
GROUP BY - collapses rows into one row per group

<img width="861" height="372" alt="image" src="https://github.com/user-attachments/assets/6d5d8b77-4e83-47eb-aa57-0c039b9924ed" />


