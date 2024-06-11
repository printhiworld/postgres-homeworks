create table employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(55),
	last_name varchar(55),
	title varchar(250),
	birth_date varchar(10),
	notes varchar(250)
);

create table customers
(
	customer_id  varchar(10) primary key,
	company_name varchar(55),
	contact_name varchar(55)
);

create table orders
(
	order_id int primary key,
	customer_id varchar(10) REFERENCES customers(customer_id),
	employee_id int references employees(employee_id) not null,
	order_date varchar(10),
	ship_city varchar(55)
);