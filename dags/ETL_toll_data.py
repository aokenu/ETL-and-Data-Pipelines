

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

    'owner': 'Goldstine',

    'start_date': days_ago(0),

    'email': ['chibuikeokenu@gmail.com'],

    'email_on_failure': True,

    'email_on_retry': True,

    'retries': 1,

    'retry_delay': timedelta(minutes=5),

}





dag = DAG(

    dag_id='ETL_toll_data',

    default_args = default_args,

    description='Apache Airflow Final Assignment',

    schedule_interval=timedelta(days=1),

)





# defining the tasks

unzip_data = BashOperator(

    task_id='unzip_data',

    bash_command="tar xzf tolldata.tgz",

    dag=dag,

)





# defining task 2

extract_data_from_csv = BashOperator(

    task_id='extract_data_from_csv',

    bash_command='cut -d","  -f1,2,3,4 vehicle-data.csv > csv_data.csv',

    dag=dag,

)





# defining task 3

extract_data_from_tsv = BashOperator(

    task_id='extract_data_from_tsv',

    bash_command='cut -d" " -f5,6,7 tollplaza-data.tsv > tsv_data.csv',

    dag=dag,

)



# defining task 4

extract_data_from_fixed_width = BashOperator(

    task_id='extract_data_from_fixed_width',

    bash_command='cut -d" " -f6,7 payment-data.txt > fixed_width_data.csv',

    dag=dag,

)



# defining task 5

consolidate_data = BashOperator(

    task_id='consolidate_data',

    bash_command='paste csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',

    dag=dag,

)





# defining task 6

transform_data = BashOperator(

    task_id='transform_data',

    bash_command='awk -F"," { print $1","$2","$3","toupper($4)","$5","$6","$7","$8","$9; } < extracted_data.cv > transformed_data.csv', 

    dag=dag,

)





# defining the task pipeline

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data