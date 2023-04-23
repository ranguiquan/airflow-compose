from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

default_args = {
    "owner": "airflow",
    "description": "Use of the DockerOperator",
    "depend_on_past": False,
    "start_date": datetime(2018, 1, 3),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
with DAG(
    "docker_dag",
    default_args=default_args,
    schedule_interval="*/2 * * * *",
    catchup=False,
) as dag:
    t1 = DockerOperator(
        task_id="docker",
        image="airflow-worker-python",
        api_version="auto",
        auto_remove=True,
        # https://stackoverflow.com/questions/52458528/executing-python-and-bash-commands-using-dockeroperator
        command='bash -c "cd scripts && python test.py"',
        docker_url="unix://var/run/docker.sock",
        network_mode="fin_pip_airflow-net",
        mounts=[
            Mount(
                source="/home/ranguiquan/workspace/project/fin_pip/scripts",
                target="/workspace/scripts",
                type="bind",
            )
        ],
    )
    t1
