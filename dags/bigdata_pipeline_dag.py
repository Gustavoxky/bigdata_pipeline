import sys
sys.path.append('/opt/airflow/src')  # Garante que o diretório src seja acessível

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.ingestion.kafka_consumer import consume_messages
from src.processing.spark_processor import SparkProcessor

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
}

def run_spark_processing():
    processor = SparkProcessor(master_url="spark://spark:7077")
    sample_data = [{"key": "1", "value": 1.2}, {"key": "2", "value": 3.4}]
    processed = processor.process_data(sample_data)
    processor.write_to_hdfs(processed, "hdfs://hadoop:9000/data/processed")

with DAG(
    "bigdata_pipeline",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    consume_task = PythonOperator(
        task_id="consume_kafka",
        python_callable=consume_messages,
        op_args=["bigdata_topic", "kafka:9092"]
    )

    process_task = PythonOperator(
        task_id="process_with_spark",
        python_callable=run_spark_processing,
    )

    consume_task >> process_task
