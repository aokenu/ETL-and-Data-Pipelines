#!/bin/sh

psql --username=postgres --host=172.17.0.2 -c "create database sales_new;"

psql --username=postgres --host=172.17.0.2 --dbname=sales_new -c "CREATE TABLE sales_data(rowid int,product_id int,customer_id int,price decimal,quantity int,timestamp timestamp,dateid SERIAL PRIMARY KEY);

create table DimDate(dateid int,day varchar(20),month varchar(30),year varchar(5));

create table FactSales(rowid int,product_id int,custome_id int,price decimal,total_price decimal);"