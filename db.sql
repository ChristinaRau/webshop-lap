-- Active: 1712601255292@@localhost@3306@computer-db
create table reseller (
    id int AUTO_INCREMENT, name varchar(255), primary key (id)
);

create table `order` (
    id int AUTO_INCREMENT, reseller_id int not null, `datetime` datetime not null, primary key (id), foreign key (reseller_id) references reseller (id)
);

create table computer_base_model (
    id int AUTO_INCREMENT, name varchar(255) not null, ram_gigabyte float not null, price float not null, storage_gigabyte float not null, processor varchar(255) not null, image_path varchar(255), description varchar(255), primary key (id)
);

create table order_computer (
    id int AUTO_INCREMENT, order_id int not null, computer_base_model_id int not null, primary key (id), foreign key (order_id) REFERENCES `order` (id), foreign key (computer_base_model_id) references computer_base_model (id)
);

create table addition (
    id int AUTO_INCREMENT, `name` varchar(255) not null, `value` varchar(255) not null, price float not null, primary key (id)
);

create table order_computer_addition (
    id int auto_increment, order_computer_id int not null, addition_id int not null, primary key (id), foreign key (order_computer_id) references order_computer (id), foreign key (addition_id) references addition (id)
);

create table user (
    id int AUTO_INCREMENT, username varchar(255) not null, password varchar(255) not null, primary key (id)
);

CREATE USER 'computershop' @'localhost' IDENTIFIED BY 'qS{MO6?>8495<';

SET PASSWORD FOR 'computershop' @'localhost' = PASSWORD ('qS{MO6?>8495<');

GRANT
SELECT,
INSERT
,
UPDATE,
DELETE,
FILE,
INDEX,
CREATE TEMPORARY TABLES,
CREATE VIEW,
EVENT,
TRIGGER,
SHOW VIEW,
EXECUTE ON *.* TO 'computershop' @'localhost';

GRANT ALL PRIVILEGES ON `computer-db`.* TO 'computershop' @'localhost'
WITH
GRANT OPTION;