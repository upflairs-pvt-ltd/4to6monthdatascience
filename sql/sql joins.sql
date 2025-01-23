show databases;
create database joindemo;
use joindemo;

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100),
    DeptID INT
);

INSERT INTO Employees (EmpID, EmpName, DeptID) VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 101),
(4, 'Diana', 103),
(5, 'Eve', NULL);

select * from Employees;

CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(100),
    Manager VARCHAR(100)
);

INSERT INTO Departments (DeptID, DeptName, Manager) VALUES
(101, 'Human Resources', 'Karen'),
(102, 'Finance', 'Tom'),
(103, 'Engineering', 'Mike');


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
select * from Projects;


select * from Employees inner join  Departments
on Employees.DeptID = Departments.DeptID;

select * from Employees inner join  projects
on Employees.Empid = projects.empid;

show tables;

select Employees.EmpID , Employees.EmpName, projects.ProjectName ,projects.ProjectID from Employees inner join  projects
on Employees.Empid = projects.empid;



select * from Employees left join  Departments
on Employees.DeptID = Departments.DeptID;


select * from Employees right join  projects
on Employees.Empid = projects.empid;

select * from Employees full  join  projects  
on Employees.EmpID = projects.EmpID;

select * from projects;


