use learning;
select min(stu_age) from studentdata;
select max(stu_age) from studentdata;
select sum(stu_age) from studentdata;
select avg(stu_age) from studentdata;
select round(avg(stu_age)) from studentdata; 
select *  from studentdata where stu_age >= 20 and stu_age <= 25;   
select * from studentdata where stu_age BETWEEN 20 and 25;

 select * from studentdata where stu_age in (20,26,18); 
 select * from studentdata where stu_age not in (20,26,18); 