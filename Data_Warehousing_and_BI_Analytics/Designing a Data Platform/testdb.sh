#!/bin/bash

DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD="root"
DB_NAME="sales"

MYSQL_CMD="mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME"

QUERY="SELECT * FROM sales_data;"

$MYSQL_CMD -e "$QUERY"
