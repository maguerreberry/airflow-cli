import click
import requests

from airflow_cli.utils.context import get_env_from_ctx
from airflow_cli.utils.request import get_auth, get_base_url


@click.command()
@click.argument("dag_id", type=str)
@click.pass_context
def list(ctx, dag_id):
    env = get_env_from_ctx(ctx)
    base_url = get_base_url(env)
    auth = get_auth(env)

    endpoint = f"dags/{dag_id}/dagRuns"

    url = f"{base_url}/{endpoint}"

    response = requests.get(url=url, auth=auth)

    print(response.text)


@click.command()
@click.argument("dag_id", type=str)
@click.argument("dag_run_id", type=str)
@click.pass_context
def clear(ctx, dag_id, dag_run_id):
    env = get_env_from_ctx(ctx)
    base_url = get_base_url(env)
    auth = get_auth(env)

    endpoint = f"dags/{dag_id}/dagRuns/{dag_run_id}/clear"

    url = f"{base_url}/{endpoint}"

    print("url", url)

    payload = {"dry_run": False}

    response = requests.post(url=url, auth=auth, json=payload)
    response.raise_for_status()
    print(response.text)


@click.group()
@click.pass_context
def dag_runs(ctx):
    pass


dag_runs.add_command(list)
dag_runs.add_command(clear)
