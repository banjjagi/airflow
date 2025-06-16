from airflow import DAG
import datetime
import pendulum

with DAG(
    dag_id='dag_bash_operator',
    start_date=pendulum.datetime(2023, 10, 1, tz="UTC"),
    schedule_interval='@daily',
    catchup=False,
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': datetime.timedelta(minutes=5),
    },
) as dag: