### Game Play Analysis - IV

#### Question
1. Each row represents a player logging in on a particular date
2. Ques = What percentage of players logged in again on the second day after their first loggedin date?

#### Approach
##### 1. Find each player's first login
player_id	first_login
1	         2024-01-01
2	         2024-01-03
3	         2024-01-01

##### 2. Check if the player logged in on first login + 1 day
player_id	first_login	login on next day?
1	2024-01-01	Yes (01-02)
2	2024-01-03	No
3	2024-01-01	Yes (01-02)

##### Players satisfying condition = 2
##### Total players = 3
##### Fraction = 2/3 = 0.67

##### One player must have logged in more times not necessarily only twice and we still need to consider that person so we should not check for how many times 
##### he logged in because that is irrelevant. We should only check if the next login date is one more than the previous.

#####################################################  
APPROACH

# Write your MySQL query statement below
SELECT ROUND((COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT(player_id)) FROM Activity)), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN(SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id)

In this inner query we are trying to return player_id and the first login date which is MIN(event_date) because we are already doing GROUP BY player_id here
so it will create different groups based on player_id. 

Once we get this result we want to use this to find out if the player has logged in the next day or not so we take the DATEDIFF of event_date or the first_login we just extracted and the INTERVAL 1 DAY will check if the next entry is the next day or not.

Now we need to find the fraction in the outer query so we do COUNT(DISTINCT player_id) in the numerator because our subquery will return a table with all the entries / logins of each player_id as a group. So we need DISTINCT here

In the denominator we need the count of all the players so we have to again write a sql select query to select all the players from the main table. If we dont do SELECT again then it will use the output that we got from group by to get the count so even in the denominator it will be 1. But we want the denominator to include all the players which is = 3

