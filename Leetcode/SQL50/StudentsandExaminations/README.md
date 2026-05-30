## 1. Understand the tables - Students, Subjects, Examinations
Students - Has student information
Subjects - Has subject information
Examinations - Each student from the Students table takes every course from the Subjects table. Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
          This saves attendance.
## 2. Find the number of times each student attended each exam.
For every (student, subject) pair show attendance count

## 3. Build the expected rows manually
Alice Math
Alice Physics
Alice Programming
Bob Math
Bob Physics
Bob Programming
etc

## 4. Approach and Edge case scenario 
Alex never appears in Exams so if we start from Examinations like FROM Examinations then we will not have any record of Alex in the output. So the combination should
be Students * Subjects. And it should be a CROSS JOIN because output requires every Student with every Subject combination even when there is no match. 

## 5. For each (student_id, subject_name) pair, how many matching rows exist in Examinations?
Check for matches between the cross join output and the Examinations table. For this LEFT JOIN is good because only a LEFT JOIN will check for all combinations
from the pair table and check if there is a match for every entry in the examination table or not.



