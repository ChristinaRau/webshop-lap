-- Active: 1712647823994@@127.0.0.1@3306@webshop-db
create table product (
    `id` int auto_increment, `name` varchar(255) not null, price float not null, image_path varchar(255), primary key (id)
);

create table address (
    `id` int auto_increment, first_name varchar(50) not null, last_name varchar(50) not null, street varchar(255) not null, house_number varchar(50) not null, zip_code varchar(50) not null, city varchar(50) not null, country varchar(50), primary key (id)
);

create table product_detail (
    `id` int auto_increment, product_id int not null, `name` varchar(50) not null, `value` varchar(255) not null, primary key (id), foreign key (product_id) references product (id)
);

create table customer (
    id int AUTO_INCREMENT, billing_address_id int not null, email_address varchar(255) not null, tel_number varchar(255), primary key (id), foreign key (billing_address_id) references `address` (`id`)
);

create table `order` (
    id int AUTO_INCREMENT, customer_id int not null, delivery_address_id int, payment_method varchar(50), date_ordered datetime, primary key (id), foreign key (customer_id) references customer (id), foreign key delivery_address_id references address (id)
);

create table order_product (
    id int AUTO_INCREMENT, order_id int not null, product_id int not null, primary key (id), foreign key (order_id) references `order` (id), foreign key (product_id) references product (id)
)