# import the libraries


from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator

# This makes scheduling easy
from airflow.utils.dates import days_ago



#defining DAG arguments
default_args = {
    'owner': 'Golstine',
    'start_date': days_ago(0),
    'email': ['chibuikeokenu@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



dag = DAG(
    dag_id='ETL_toll_data',
    default_args = default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)


# defining the task1
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -zxvf /opt/airflow/logs/tolldata.tgz -C /opt/airflow/logs/',
    dag=dag,
)



# defining task 2
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d","  -f1,2,3,4 /opt/airflow/logs/vehicle-data.csv > /opt/airflow/logs/csv_data.csv',
    dag=dag,
)


# defining task 3
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -d" " -f5,6,7 /opt/airflow/logs/tollplaza-data.tsv > /opt/airflow/logs/tsv_data.csv',
    dag=dag,
)


# defining task 4
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -d" " -f6,7 /opt/airflow/logs/payment-data.txt > /opt/airflow/logs/fixed_width_data.csv',
    dag=dag,
)


# defining task 5
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste /opt/airflow/logs/csv_data.csv /opt/airflow/logs/tsv_data.csv /opt/airflow/logs/fixed_width_data.csv > /opt/airflow/logs/extracted_data.csv',
    dag=dag,
)



# defining task 6
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="awk 'BEGIN {FS=OFS=\",\"} { $4= toupper($4) } 1' /opt/airflow/logs/extracted_data.csv > /opt/airflow/logs/transformed_data.csv", 
    dag=dag,
)



# defining the task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
