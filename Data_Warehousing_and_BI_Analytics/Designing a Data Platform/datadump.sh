#!/bin/bash

# MySQL database connection details
DB_USER="root"
DB_PASSWORD="root"
DB_NAME="sales"

# Output file
OUTPUT_FILE="sales_data.sql"

# MySQL query to export data
MYSQL_QUERY="SELECT * FROM sales_data;"

# Run MySQL query and export data to a file
mysqldump -u"${DB_USER}" -p"${DB_PASSWORD}" "${DB_NAME}" --skip-add-locks --skip-lock-tables --hex-blob --result-file="${OUTPUT_FILE}" --skip-triggers --skip-comments --no-create-info --skip-tz-utc --compact --skip-extended-insert --quick --skip-set-charset --skip-quote-names -e -q -c --skip-opt -B "${DB_NAME}" --tables sales_data

# Check if the export was successful
if [ $? -eq 0 ]; then
  echo "Data exported successfully to ${OUTPUT_FILE}"
else
  echo "Error exporting data. Check your MySQL credentials and try again."
fi
