-- select count(*) from Customers;

-- aggregate: sum, count , min , max ,avg 
-- select sum(age) from Customers;
-- select min(age) from Customers;
-- select max(age) from Customers;
-- select avg(age) from Customers;

-- select age, first_name,country from Customers;
-- select * from CUSTOMERS  WHERE COUNTRY = "USA";
-- select first_name,country,AGE from Customers where country = "USA" order by age;
-- select first_name,country,AGE from Customers where country = "USA" order by age desc;  --descending order 
-- select first_name,country,AGE from Customers where country = "USA" order by age desc limit 1;

-- select * from Customers limit 3 offset 2;

--select item,amount from orders where customer_id = 4 AND amount >350;

-- select * from customers where country = "USA" or country = "UAE";
-- select * from customers where country = "USA" AND country = "UAE";

-- SELECT * from shippings where status != 'Pending';
-- SELECT * from shippings where status != 'Pending';
-- SELECT * from shippings where status <>  'Pending';
-- select * from shippings where not status = "Pending";

-- select * from customers where age >=22 and age <= 25;
-- select * from customers where age between 22 and  25 ;
-- union and union all
select  first_name ,age from customers
union 
select age , first_name    from customers







