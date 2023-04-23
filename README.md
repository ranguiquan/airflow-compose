## About The Project

This is a template of Airflow docker setup which is compatible with docker operator.
The template is Python oriented but should work well with other languages.



![](https://cdn.jsdelivr.net/gh/rgqsimg/picBed/PicGo/2023/04/23-23-06-36-15a2dbec2bfad6a544383526ee865b6a-20230423230635-3e2b79.png)

## Environment

WSL 2 works for me. Not sure about macOS and Windows.

## Set Up

Clone this repository.

Run

```bash
$ mkdir logs && echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Prepare a `requirements.txt`, copy it to the root of the folder. Build the Python worker image. Run

```bash
$ docker build -t airflow-worker-python -f Dockerfile.worker.python .
```

Change permission of  `/var/run/docker.sock`

```bash
$ sudo chmod 666 /var/run/docker.sock
```

Go to [`./dags/example.py`]('https://github.com/ranguiquan/airflow-compose/blob/dags/example.py'), find all the `TODO:` marks, check the comments and modify some values.

## Build Workflow with it

Since you can bind your source code to the container, there is no need to change your old projects, as long as they have some explicit entry points.

First, build a image for your project runtime. To generate `requirements.txt`, you can use

```bash
$ poetry export -f requirements.txt -o requirements.txt
$ # or
$ pip freeze > requirements.txt
```

Then choose a proper name for the image, move to the `./dags` file. Create a dag with docker operator in it. Remember to mount your source code to the container's workspace and define the command.
