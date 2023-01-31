"""
This type stub file was generated by pyright.
"""

import click
from celery.bin.base import (
    ISO8601,
    ISO8601_OR_FLOAT,
    JSON_ARRAY,
    JSON_OBJECT,
    CeleryCommand,
    CeleryOption,
    handle_preload_options,
)

"""The ``celery call`` program used to send tasks from the command-line."""

@click.command(cls=CeleryCommand)
@click.argument("name")
@click.option(
    "-a",
    "--args",
    cls=CeleryOption,
    type=JSON_ARRAY,
    default="[]",
    help_group="Calling Options",
    help="Positional arguments.",
)
@click.option(
    "-k",
    "--kwargs",
    cls=CeleryOption,
    type=JSON_OBJECT,
    default="{}",
    help_group="Calling Options",
    help="Keyword arguments.",
)
@click.option(
    "--eta",
    cls=CeleryOption,
    type=ISO8601,
    help_group="Calling Options",
    help="scheduled time.",
)
@click.option(
    "--countdown",
    cls=CeleryOption,
    type=float,
    help_group="Calling Options",
    help="eta in seconds from now.",
)
@click.option(
    "--expires",
    cls=CeleryOption,
    type=ISO8601_OR_FLOAT,
    help_group="Calling Options",
    help="expiry time.",
)
@click.option(
    "--serializer",
    cls=CeleryOption,
    default="json",
    help_group="Calling Options",
    help="task serializer.",
)
@click.option(
    "--queue", cls=CeleryOption, help_group="Routing Options", help="custom queue name."
)
@click.option(
    "--exchange",
    cls=CeleryOption,
    help_group="Routing Options",
    help="custom exchange name.",
)
@click.option(
    "--routing-key",
    cls=CeleryOption,
    help_group="Routing Options",
    help="custom routing key.",
)
@click.pass_context
@handle_preload_options
def call(
    ctx,
    name,
    args,
    kwargs,
    eta,
    countdown,
    expires,
    serializer,
    queue,
    exchange,
    routing_key,
):  # -> None:
    """Call a task by name."""
    ...
