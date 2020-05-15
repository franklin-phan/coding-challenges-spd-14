#Write a SQL query to get the second highest salary from the Employee table.

# Restate the problem- sort the salaries and get the second highest
# Ask clarifying questions- how many salaries will I have to deal with?
# State your assumptions- whole numbers, already sorted
# Think out loud-we need to get the last index minus 1
# Brainstorm solutions-compare evert single salary to get the second highest
# Explain your rationale- it's naive but one of the easiest to implement
# Discuss trade offs - speed, we have to traverse every salaray
# Suggest improvements- work on speed, find a way to only get the last two salaries

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)

#dupicate emails
# Restate the problem- find repeating emails
# Ask clarifying questions- how many emails
# State your assumptions-emails are alphabetically sorted
# Think out loud-how do we find the fastest way to traverse every email?
# Brainstorm solutions- check every email to the other
# Explain your rationale-naive solution, easy to implement
# Discuss trade offs- very slow
# Suggest improvements-binarysearch, maybe


SELECT DISTINCT p1.Email
FROM Person p1, Person p2
WHERE p1.Email = p2.Email and p1.id != p2.id
;