from airflow import DAG
from airflow.operators.bash_operator import BashOperator
# from datetime import datetime, timedelta
import datetime as dt


dag = DAG(
    'test_dag',
    start_date=dt.datetime(2020, 1, 12, 18, 29, 00),
    schedule_interval="*/15 * * * *"
)

t1 = BashOperator(
    task_id='print_date2',
    bash_command='date',
    dag=dag
)
