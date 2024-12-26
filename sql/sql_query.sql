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
use upflairs;
show tables;
select * from studentdata;

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







