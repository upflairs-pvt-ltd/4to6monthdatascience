show databases;
create database upflairs;
USE world;
show tables;
select * from city;
select Name , District FROM city;

use upflairs;
show tables;

-- create table  

create table studentdata (student_id INT ,student_name varchar(30) , student_rollno INT , student_branch varchar(20), student_city varchar(35));
show tables;
select * from studentdata;
desc studentdata;

;
ALTER TABLE studentdata ADD
college_city VARCHAR(30);

DROP DATABASE upflairs;
DROP TABLE studentdata;
show tables;
show databases;

desc studentdata;
select * from studentdata;

INSERT INTO studentdata (student_id,student_name,student_rollno,student_branch,student_city,college_city)
values (1,"Radhey",101,"cse","mathura","jaipur");


INSERT INTO studentdata values (6,"Mohan",109,"it","jaipur","kota");



INSERT INTO studentdata VALUES 
(2, 'Rohit', 103, 'CS', 'Delhi', 'Delhi'),
(3, 'Priya', 104, 'ECE', 'Mumbai', 'Mumbai'),
(4, 'Amit', 105, 'ME', 'Bangalore', 'Bangalore'),
(5, 'Sneha', 106, 'EE', 'Jaipur', 'Jaipur');


select * from studentdata;
select * from studentdata where student_city="jaipur";

TRUNCATE TABLE studentdata;
DROP TABLE studentdata;

SET SQL_SAFE_UPDATES = 0;
-- SET SQL_SAFE_UPDATES = 1;
delete  from studentdata where student_city="jaipur";
select * from studentdata;

show databases;
use  flaskapp;
show tables;
desc contactdata;
drop table contactdata;


show databases;
use upflairs;
show tables;
select * from studentdata;
select * from contactdata;

update studentdata SET student_name = "Priya" where student_rollno = 104;

update studentdata SET student_branch = "CSE" where student_rollno >= 104;
update studentdata SET student_city = "DELHI" where student_branch = "CSE";


delete , drop , truncate 
drop ==> database or table  (object + data) 
delete ==> to delete specific data 
truncate  ==> object safe (data loss) 
drop table studentdata;
truncate studentdata;
show tables;
select * from studentdata;
drop table studentdata;
delete  from studentdata where student_branch="CS";



show tables
use upflairs;





-- Create the Employees table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100),
    DeptID INT
);

-- Insert data into Employees
INSERT INTO Employees (EmpID, EmpName, DeptID) VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 101),
(4, 'Diana', 103),
(5, 'Eve', NULL);

-- Create the Departments table
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(100),
    Manager VARCHAR(100)
);

-- Insert data into Departments
INSERT INTO Departments (DeptID, DeptName, Manager) VALUES
(101, 'Human Resources', 'Karen'),
(102, 'Finance', 'Tom'),
(103, 'Engineering', 'Mike');

-- Create the Projects table
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(100),
    EmpID INT
);

-- Insert data into Projects
INSERT INTO Projects (ProjectID, ProjectName, EmpID) VALUES
(1001, 'Project Alpha', 1),
(1002, 'Project Beta', 2),
(1003, 'Project Gamma', 3),
(1004, 'Project Delta', 4),
(1005, 'Project Epsilon', NULL);






show tables;

select * from  projects;

select * from employees INNER JOIN projects on employees.EmpID = projects.EmpID;

-- alias 

select * from employees as e INNER JOIN projects as p on e.EmpID = p.EmpID;

select EmpName ,ProjectName , DeptID from employees as e INNER JOIN projects as p on e.EmpID = p.EmpID;



select e.DeptID , e.EmpName ,p.ProjectName , e.EmpID from employees as e 
INNER JOIN projects as p on e.EmpID = p.EmpID
where e.DeptID = 101;


select e.DeptID , e.EmpName ,p.ProjectName , e.EmpID from employees as e 
right JOIN projects as p on e.EmpID = p.EmpID;


select * from employees
FULL JOIN projects;

select * from employees
natural JOIN projects;


select * from projects
natural JOIN departments;


show databases;
use upflairs
show tables;


create table B (test2 int);
INSERT INTO B (test2) 
values(5),(6),(7);
select * from B;

select * from A cross join B;
select * from A,B;





-- Create the Employees table
CREATE TABLE Emp (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    ManagerID INT
);

-- Insert records into the Employees table
INSERT INTO Emp (EmployeeID, Name, ManagerID)
VALUES
(1, 'Alice', NULL),  -- Alice is the top-level manager
(2, 'Bob', 1),       -- Bob reports to Alice
(3, 'Carol', 1),     -- Carol reports to Alice
(4, 'David', 2);     -- David reports to Bob


select * from emp;

select *  from emp as e1 
inner join emp as e2 on e1.EmployeeID = e2.ManagerID;

select *  from emp as e1 
left join emp as e2 on e1.EmployeeID = e2.ManagerID;





-- Create the Employees table
CREATE TABLE Emp2 (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

-- Insert 15 records into the Employees table
INSERT INTO Emp2 (EmployeeID, Name, Department, Salary)
VALUES
(1, 'Alice', 'HR', 50000),
(2, 'Bob', 'IT', 60000),
(3, 'Carol', 'HR', 55000),
(4, 'David', 'Finance', 70000),
(5, 'Eve', 'IT', 65000),
(6, 'Frank', 'Finance', 72000),
(7, 'Grace', 'HR', 52000),
(8, 'Hank', 'IT', 67000),
(9, 'Ivy', 'Marketing', 58000),
(10, 'Jack', 'Marketing', 60000),
(11, 'Kathy', 'Finance', 75000),
(12, 'Liam', 'IT', 63000),
(13, 'Mona', 'HR', 54000),
(14, 'Nancy', 'Marketing', 62000),
(15, 'Oscar', 'Finance', 80000);


select  name,  max(salary) from emp2 where Department = "HR";

SELECT  MAX(salary) 
FROM emp2 
WHERE Department = 'HR';

select Department, count(*) from emp2
group by Department;

select Department, count(*) as no_of_count from emp2
group by Department;


select Department, avg(salary) as max_salary from emp2
group by Department  order by max_salary limit 2 ;


select Department, avg(salary) as average_salary from emp2
group by Department having average_salary > 60000;

select  distinct(Department) from emp2;


select count(*) from emp2 where department = "HR" or department = "IT";
select count(*) from emp2 where department in ("HR","IT");
select * from emp2 where department in ("HR","IT");
select * from emp2 where department not in ("HR","IT");

show databases;
use laptop;
show tables;
select * from table_name;



show databases;
create database learning;
drop database learning;

use learning;


create table studentdata (stu_rollno int,  stu_name  varchar(25), stu_age int, stu_course varchar(25));
show tables;
drop table studentdata;

desc studentdata;

select * from studentdata;
SELECT * FROM studentdata;

insert into studentdata (stu_rollno ,  stu_name , stu_age , stu_course)
values (3,"Nikita",24,"IT");


insert into studentdata values (3,"Nikita",24,"IT");

insert into studentdata 
values (4,"saniya",25,"BSC"),
    	(5,"ayush",26,"CSE"),
        (6,"laksya",25,"CSE");


SELECT * FROM studentdata;
SELECT stu_name, stu_course  FROM studentdata;




CREATE TABLE feesrecord (
  st_name varchar(25),
  st_course varchar(25),
  st_fees varchar(4),
  fee_amount int,
  fees_date date
);

show tables;
insert into feesrecord values("anshika","cse","yes",250,"2025-01-05");


show databases;
use learning;
show tables;
select * from studentdata;

select * from feesrecord;
delete drop truncate 

SET SQL_SAFE_UPDATES = 0;

DELETE  from studentdata  where stu_course="BSC";

select * from studentdata;
select * from feesrecord;
truncate feesrecord;
show tables;

select * from studentdata where stu_course='cse';
select * from studentdata where stu_age <= 25;

select * from studentdata where stu_age <= 25 and stu_course='IT';
select * from studentdata where stu_age <= 25 or stu_course='IT';


select * from feesrecord;

ALTER table feesrecord ADD column due_fee int;
ALTER table feesrecord ADD  due_fees int;

ALTER table feesrecord DROP column due_fee;
ALTER table feesrecord DROP  due_fee;

ALTER table feesrecord CHANGE due_fees fees_due int;

alter table feesrecord RENAME column fees_due to due_fees;
UPDATE  studentdata   SET stu_name = "Sania"  where stu_rollno=6;
select * from studentdata;

update studentdata set stu_age=20 where stu_course="it" and stu_name="anshika";

select * from studentdata;

show databases; 
use learning;
show tables;
select stu_name,stu_age from studentdata;
select * from studentdata where stu_course="IT";
select * from studentdata where stu_age <= 25 or stu_course="IT";


select * from feesrecord;
drop table feesrecord; 
truncate feesrecord;

SET SQL_SAFE_UPDATES = 0;

delete from studentdata where stu_name='ayush';
delete from studentdata where stu_age <= 25;
select * from studentdata;

update studentdata set stu_course="civil" where stu_name = "sania";
update studentdata set stu_course = "civil" where stu_age <= 25;

select * from studentdata; 
alter table studentdata add column extra int;
alter table studentdata add  extra2 int; 
alter table studentdata drop column extra2;
alter table studentdata drop  extra;

show tables;
show databases;
use joindemo;

select * from employees natural join departments;
select * from  projects;

select * from departments natural join projects;

select * from departments cross join projects;

select min(DeptId) from departments;
select max(DeptId) from departments;
select avg(DeptId) from departments;
select sum(DeptId) from departments;

select round(avg(DeptId),2) from departments;

show databases;
use learning;
select distinct  stu_course from studentdata;

select * from studentdata order by stu_age;
select * from studentdata order by stu_age desc;
select * from studentdata order by stu_age desc limit 3;
select * from studentdata order by stu_age desc limit 3 offset 1;

show databases;


