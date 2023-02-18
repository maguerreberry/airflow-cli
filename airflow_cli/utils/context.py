from dataclasses import dataclass

from click import Context

from airflow_cli.conf.environment import Env


@dataclass
class UserContext:
    env: Env


def get_env_from_ctx(ctx: Context) -> Env:
    user_context: UserContext = ctx.obj
    return user_context.env


def set_env_from_ctx(ctx: Context, env: Env) -> None:
    ctx.obj = UserContext(env)
