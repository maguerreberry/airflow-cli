import click
from click import Context

from airflow_cli.conf.environment import EnvPrd, EnvStg
from airflow_cli.groups.connections import connections
from airflow_cli.groups.dag_runs import dag_runs
from airflow_cli.groups.dags import dags
from airflow_cli.utils.context import set_env_from_ctx


@click.group()
@click.option(
    "--env",
    default="stg",
    help="Airflow environment to connect to.",
    type=click.Choice(["stg", "prd"]),
)
@click.pass_context
def main(ctx: Context, env: str):
    env_class = EnvPrd if env == "prd" else EnvStg
    set_env_from_ctx(ctx, env_class)


main.add_command(connections)
main.add_command(dags)
main.add_command(dag_runs)

if __name__ == "__main__":
    main()
