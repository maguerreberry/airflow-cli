from requests.auth import HTTPBasicAuth

from airflow_cli.conf.environment import Env


def get_base_url(env: Env) -> str:
    return f"https://{env.host}/api/v1"


def get_auth(env: Env) -> HTTPBasicAuth:
    return HTTPBasicAuth(env.user.encode("utf-8"), env.password.encode("utf-8"))
