import os

from dotenv import load_dotenv

load_dotenv()


class Env:
    host: str
    user: str
    password: str


class EnvStg(Env):
    host: str = os.getenv("AIRFLOW_HOST_STG")
    user: str = os.getenv("AIRFLOW_USER_STG")
    password: str = os.getenv("AIRFLOW_PASSWORD_STG")


class EnvPrd(Env):
    host: str = os.getenv("AIRFLOW_HOST_PRD")
    user: str = os.getenv("AIRFLOW_USER_PRD")
    password: str = os.getenv("AIRFLOW_PASSWORD_PRD")
