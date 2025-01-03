from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/opt/airflow/src')  # Adicione este trecho para incluir o diretório no path

from src.main import main

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="bigdata_pipeline",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_bigdata_pipeline",
        python_callable=main,
    )

    run_pipeline
