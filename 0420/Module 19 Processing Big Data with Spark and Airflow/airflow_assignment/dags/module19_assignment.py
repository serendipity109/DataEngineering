from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow.utils.dates import days_ago


default_args = {
    'owner': 'Wang',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['jayda960825@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def square(x):
    return x * x


dag = DAG(
    'python_square_operator',
    description = 'Squaring a number using Airflow',
    schedule_interval = "0 12 * * *",
    start_date = datetime(2017,3,20))


t1 = PythonOperator(
    task_id='square',
    python_callable=lambda: square(13),
    dag=dag,
)