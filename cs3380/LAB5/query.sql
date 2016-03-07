/3.3.1 Create a View: Part 1
Create a view that shows the person’s id (pid), first name (fname) and last name (lname) for all people who
have a body weight above 140. This view should be named “weight” (without the quotes). You must use an
INNER JOIN in the views query. Your PHP page should then query the view (i.e. SELECT * FROM weight).
(8 rows)
3.3.2 Create a View: Part 2
Create a view that returns the first name (fname), last name (lname) and BMI for people with a weight
above 150. This view should be named “BMI”. You must use an INNER JOIN and you must reference the
“weight” view created in 3.3.1. BMI is calculated as
703 ·
weight
height2
(1)
In this view, round the BMI value to the nearest whole number. For example, a person with a height of 71
inches and weight of 145 lbs would have a BMI of 20.2 which would be rounded to 20. Use an SQL function
2
to achieve this rounded result. Your PHP page should then query the view (i.e. SELECT * FROM bmi). (12
8 rows)
3.3.3 Using EXISTS
Write a query that shows returns the name and city of the university that has no people in database that
are associated with it. Your query must use EXISTS to achieve. (2 rows)
3.3.4 Using IN
Write a query that returns only the uid value for all universities in the city Columbia. Then use that query
with an IN sub-query expression to retrieve the first and last names for all people that go to school in
Columbia. (4 rows)
3.3.5 Using NOT IN
Write a query that returns all of the activities with records in the participated in table. Then use that
query with a NOT IN sub-query expression to retrieve the activities that are not played by any player in the
database. (2 rows)
3.3.6 Using UNION
Write a query that returns the pid of all people listed in participated in that participate in ‘running’.
Then modify your query to use UNION to return all people who run or play racquetball. You must use the
UNION operator to accomplish this. You cannot use OR. (5 Rows)
3.3.7 Using INTERSECTS
Write a query that returns the first and last name of all people listed in body composition table who are
older than 30 years old. Then modify your query to use INTERSECTS to return all people who are older than
30 and are taller than 65 inches. You must use the INTERSECTS operator to accomplish this. You cannot
use AND. (3 rows)
3.3.8 Using ORDER BY
Write a query that returns peoples first and last names weight, height, and age. Records should be ordered
first by height in descending (Z-to-A order), then by weight in ascending order, and finally by the person’s
last name in ascending order. (12 rows)

*/

#Query 1
CREATE VIEW weight SELECT person.pid,fname,lname FROM person INNER JOIN body_composition ON person.pid=body_composition.pid WHERE weight >140;

#Query 2


#Query 3
SELECT university_name,city FROM university WHERE NOT EXISTS (SELECT * FROM person WHERE university.uid=person.uid);

#Query 4
SELECT fname,lname FROM person WHERE person.uid IN (SELECT university.uid FROM university WHERE university.city="Columbia");

#Query 5
SELECT activity.activity_name FROM activity WHERE activity.activity_name NOT IN (SELECT participated_in.activity_name FROM participated_in);
#Query 6
SELECT pid FROM participated_in WHERE activity_name = 'running' UNION SELECT pid FROM participated_in WHERE activity_name = 'racquetball';

#Query 7
SELECT DISTINCT new1.fname,new1.lname FROM person AS new1 INNER JOIN body_composition as new2 ON new1.pid=new2.pid  WHERE new2.age> 30 AND new2.age IN (SELECT age FROM person INNER JOIN body_composition ON person.pid=body_composition.pid  WHERE height >65);

#Query 8
SELECT fname,lname,weight,height,age FROM person INNER JOIN body_composition ON  person.pid=body_composition.pid ORDER BY height DESC, weight ASC, lname ASC;     