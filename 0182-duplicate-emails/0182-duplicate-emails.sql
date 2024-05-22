# Write your MySQL query statement below
SELECT email FROM Person GROUP BY Person.email HAVING COUNT(*) >1;