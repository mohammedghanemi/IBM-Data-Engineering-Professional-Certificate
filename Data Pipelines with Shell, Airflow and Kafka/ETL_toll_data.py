# Create imports
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
# DAG argument
default_args = {
    'owner': 'Mohammed_ghanemi',  
    'start_date': datetime.today(),
    'email': ['mo.ghanemi.tumei@gmail.com'], 
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
# DAG Definition
dag = DAG(
    dag_id='ETL_toll_data',
    description='Apache Airflow Final Assignment',
    default_args=default_args,
    schedule_interval='@daily',
)

# BashOperator task include 6 Tasks
# 1- UNZIP DATA
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/staging/',
    dag=dag
)

# 2- extract_data_from_csv
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="cut -d',' -f1,2,3,5 /home/project/airflow/dags/finalassignment/staging/vehicle-data.csv > /home/project/airflow/dags/finalassignment/staging/csv_data.csv",
    dag=dag
)

# 3- extract_data_from_tsv
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -f2,3,4 /home/project/airflow/dags/finalassignment/staging/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/staging/tsv_data.csv",
    dag=dag
)

# 4- extract_data_from_fixed_width
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="awk '{print substr($0,1,3) \",\" substr($0,4,3)}' /home/project/airflow/dags/finalassignment/staging/payment-data.txt > /home/project/airflow/dags/finalassignment/staging/fixed_width_data.csv",
    dag=dag
)

# 5- consolidate_data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d',' /home/project/airflow/dags/finalassignment/staging/csv_data.csv /home/project/airflow/dags/finalassignment/staging/tsv_data.csv /home/project/airflow/dags/finalassignment/staging/fixed_width_data.csv > /home/project/airflow/dags/finalassignment/staging/extracted_data.csv",
    dag=dag
)

# 6- Transform_data 
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="awk -F',' '{OFS=\",\"; $4=toupper($4); print}' /home/project/airflow/dags/finalassignment/staging/extracted_data.csv > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv",
    dag=dag
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data

