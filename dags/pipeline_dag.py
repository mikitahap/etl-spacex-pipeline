from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))

from extract import Extractor
from transform import Transformer
from load import Loader

extractor = Extractor()
transformer = Transformer()
loader = Loader()

etl_data = {}

def extract_task(**kwargs):
    extractor.extract()
    return True

def transform_task(**kwargs):
    ti = kwargs['ti']
    modified_data = transformer.transform()
    return modified_data

def load_task(**kwargs):
    ti = kwargs['ti']
    modified_data = ti.xcom_pull(task_ids='transform')
    loader.load(modified_data)

with DAG(
    dag_id="etl_dag",
    start_date=datetime(2025, 8, 17),
    schedule_interval = "@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract_task,
        provide_context=True
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform_task,
        provide_context=True
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load_task,
        provide_context=True
    )

    t1 >> t2 >> t3