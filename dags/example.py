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
    "example-dag",
    default_args=default_args,
    schedule_interval="*/2 * * * *",
    catchup=False,
) as dag:
    t1 = DockerOperator(
        task_id="docker",
        # TODO: image name should be changed to the real image name
        image="airflow-worker-python",
        api_version="auto",
        auto_remove=True,
        # https://stackoverflow.com/questions/52458528/executing-python-and-bash-commands-using-dockeroperator
        # TODO: Enter the project file and run it
        command='bash -c "cd scripts && python example.py"',
        docker_url="unix://var/run/docker.sock",
        # TODO: Check network name
        network_mode="airflow-compose_net",
        mounts=[
            Mount(
                # TODO: Change it to full path of scripts
                source="/home/ranguiquan/workspace/airflow-compose/scripts",
                target="/workspace/scripts",
                type="bind",
            )
        ],
    )
    t1
