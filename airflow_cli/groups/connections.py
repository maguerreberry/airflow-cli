import click
import requests
from click import Context
from requests.auth import HTTPBasicAuth

from airflow_cli.utils.context import get_env_from_ctx
from airflow_cli.utils.request import get_auth, get_base_url


@click.command()
@click.pass_context
def list(ctx: Context):
    env = get_env_from_ctx(ctx)
    base_url = get_base_url(env)
    auth = get_auth(env)

    endpoint = "connections"

    url = f"{base_url}/{endpoint}"

    response = requests.get(url=url, auth=auth)

    print(response.text)


@click.group()
@click.pass_context
def connections(ctx: Context):
    pass


connections.add_command(list)
