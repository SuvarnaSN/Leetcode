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

##### 
