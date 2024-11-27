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
