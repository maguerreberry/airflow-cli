import click
import requests

from airflow_cli.utils.context import get_env_from_ctx
from airflow_cli.utils.request import get_auth, get_base_url


@click.command()
@click.pass_context
def list(ctx):
    env = get_env_from_ctx(ctx)
    base_url = get_base_url(env)
    auth = get_auth(env)

    endpoint = "dags"

    url = f"{base_url}/{endpoint}"

    response = requests.get(url=url, auth=auth)

    print(response.text)


@click.group()
@click.pass_context
def dags(ctx):
    pass


dags.add_command(list)
