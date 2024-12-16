create table user(
customerID int primary key AUTO_INCREMENT,
loanAmount int,
employeeType ENUM("salaried","self employee(business)","self employee(professional)"),
netincome int,
full_name varchar(20),
phone_no varchar(20),
email varchar(20),
pan_no varchar(10),
DOB date,
pin int,
gender enum('male','female'),
address varchar(30),
past_loan enum('yes','no'),
credit_card enum('yes','no'),
purpose_of_loan varchar(40),
credit_score int
);

create table lenders(
lenderID int primary key AUTO_INCREMENT,
componey_name varchar(10),
lender_phone_no int,
max_amount int,
interest_rate int,
min_creditscore int
);

create table loan(
loanID int primary key AUTO_INCREMENT,
loan_term varchar(10),
start date,
end date
);

create table status(
online enum('pending','approved'),
employee_approvel enum('pending','approved'),
lender_approvel enum('pending','approved')
);

create table payment(
paymentID int primary key AUTO_INCREMENT,
payment_amount int,
paymnet_date date,
payment_time time,
payment_type enum('withdrawal','deposit')
);




alter table user add column lenderID int;
alter table user add foreign key(lenderID) REFERENCES lenders(lenderID);

alter table loan add column lenderID int;
alter table loan add foreign key(lenderID) REFERENCES lenders(lenderID);
alter table loan add column customerID int;
alter table loan add foreign key(customerID) REFERENCES user(customerID);


alter table payment add column lenderID int;
alter table payment add foreign key(lenderID) REFERENCES lenders(lenderID);
alter table payment add column customerID int;
alter table payment add foreign key(customerID) REFERENCES user(customerID);

alter table status add column customerID int;
alter table status add foreign key(customerID) REFERENCES user(customerID);










