/* Countries *******************************************************************/
DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
  name VARCHAR(255), continent VARCHAR(255), area INT, population INT, gdp INT
);
INSERT INTO countries (name, continent, area, population, gdp) VALUES
  ( 'Afghanistan', 'Asia', '652230', '25500100', '203430000' ),
  ( 'Albania', 'Europe', '28748', '2831741', '129600000' ),
  ( 'Algeria', 'Africa', '2381741', '37100000', '1886810000' ),
  ( 'Andorra', 'Europe', '468', '78115', '37120000' ),
  ( 'Angola', 'Africa', '1246700', '20609294', '1009900000' );

-- Select big countries: area > 3000000 OR population > 25000000:
SELECT name FROM countries AS C WHERE C.area > 3000000 OR C.population > 25000000;


/* Movies **********************************************************************
Description
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
查找 id 为奇数，并且 description 不是 boring 的电影，按 rating 降序。

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
*/
select * from movies
  where id % 2 = 1 and description != 'boring'
  order by rating desc

drop table is EXISTS movies
create table movies (
  movie varchar(128) not null unique, description text, rating float
);
insert into movies (movie, description, rating) VALUES
  ('Learn ABC', 'Interesting', 4.5),
  ('Learn Meditate', 'Interesting', 4.5),
  ('Unbound', 'Interesting', 4.5);


/* Classes More Than 5 Students ***************************************************
Description
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
查找有五名及以上 student 的 class。

+---------+
| class   |
+---------+
| Math    |
+---------+
*/

select class from classes group by class having count(distinct student) >= 5;

DROP TABLE
IF
    EXISTS courses;
CREATE TABLE courses ( student VARCHAR ( 255 ), class VARCHAR ( 255 ) );
INSERT INTO courses ( student, class )
VALUES
    ( 'A', 'Math' ),
    ( 'B', 'English' ),
    ( 'C', 'Math' ),
    ( 'D', 'Biology' ),
    ( 'E', 'Math' ),
    ( 'F', 'Computer' ),
    ( 'G', 'Math' ),
    ( 'H', 'Math' ),
    ( 'I', 'Math' );

/* Duplicate Emails *****************************************************************
Description
邮件地址表：

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
查找重复的邮件地址：

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
*/

select email from emails group by email having count(*) > 1;

drop table if EXISTS emails;
create table emails (id int primary not null, email text distinct);
insert into emails (email) VALUES
  ( 1, 'abc@abc.com', );

/* Delete Duplicate Emails
Description
邮件地址表：

+----+---------+
| Id | Email   |
+----+---------+
| 1  | john@example.com |
| 2  | bob@example.com |
| 3  | john@example.com |
+----+---------+
删除重复的邮件地址：

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
*/

-- using multiple tables
delete e1 from Emails e1, Emails e2 where e1.email = e1.email and e1.id > e2.id;

-- using set & group, min
delete from Emails where id not in (
  select min(id) as id from Emails group by email
)

drop table if EXISTS Emails;
create table Emails (id int primary, email text);
insert into Emails (id, email) VALUES 
  (1, 'a@b.c'),
  (2, 'a@d.c'),
  (2, 'a@b.c');


/* Combine Two Tables */

select FirstName, LastName, City, State
  from Person as P left join Address as A
  on A.PersonId = P.PersonId;

/* Employees Earning More Than Their Managers */
select Name, Salary, ManagerId from Employee E1, Employee E2
  where E1.ManagerId = E2.Id and E1.Salary > E2.Salary;

select Name, Salary, ManagerId from Employee E1 inner join Employee E2
  on E1.ManagerId = E2.Id and E1.Salary > E2.Salary;

/* */

select * from Customers where id not in (
  select distinct(CustomerId) from orders
)

select E.name as EmployeeName, max(Salary), D.name as DepartmentName from Employee E, Department D
  group by DepartmentId
  order by Salary desc

select salary as SecondHighestSalary from Salary
  order by salary desc
  limit 1,1;

select id - 1 as id, student
  from Seat S1 where id % 2 = 0
union
select id - 1 as id, student
  from Seat S2 where id % 2 = 1 and id != (select max(id) as id from Seat)
union
select id, student from Seat S3 where id = (select max(id) from Seat)
