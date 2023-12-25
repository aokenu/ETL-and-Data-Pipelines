#!/bin/sh

# touch  /var/tmp/sales.csv

## Write your code here to load the data from sales_data table in Mysql server to a sales.csv.
mysql --host=172.17.0.2 --port=3306 --user=root --password=root --database=sales -e "SELECT * INTO OUTFILE '/var/tmp/sales.csv'
FIELDS TERMINATED BY ','
FROM sales_data;"
## Select the data which is not more than 4 hours old from the current time.


 export PGPASSWORD=root;



 psql --username=postgres --host=172.17.0.3 --dbname=sales_new -c "\COPY sales_data(rowid,product_id,customer_id,price,quantity,timestamp) FROM '/home/datang/Downloads/sales.csv' delimiter ',' csv header;" 

 ## Delete sales.csv present in location /home/project
 sudo rm /home/datang/Downloads/sales.csv

 ## Write your code here to load the DimDate table from the data present in sales_data table

 psql --username=postgres --host=172.17.0.3 --dbname=sales_new -c  "INSERT INTO DimDate(dateid, day, month, year)
SELECT dateid, to_char(timestamp, 'day') AS day, to_char(timestamp, 'mon') AS month, to_char(timestamp, 'year') AS year
FROM sales_data;"

## Write your code here to load the FactSales table from the data present in sales_data table

psql --username=postgres --host=172.17.0.3 --dbname=sales_new -c  "INSERT INTO factsales(rowid, product_id, customer_id, price, total_price)
SELECT rowid, product_id, customer_id, price, (price * quantity) AS total_price
FROM sales_data;"

 ## Write your code here to export DimDate table to a csv

 psql --username=postgres --host=172.17.0.3 --dbname=sales_new -c "COPY DimDate TO '/var/tmp/DimDate.csv' WITH CSV HEADER;"

 ## Write your code here to export FactSales table to a csv
 
 psql --username=postgres --host=172.17.0.3 --dbname=sales_new -c "COPY FactSales TO '/var/tmp/FactSales.csv' WITH CSV HEADER;"

