import json
import requests
import click
from enum import Enum
from typing import Dict, List, Optional, Union

class Environment(Enum):
    """Environment enum."""
    DEV = 'dev'
    STAGING = 'staging'
    PROD = 'prod'

@click.group()
@click.option('--env',
            type=click.Choice([e.value for e in Environment], case_sensitive=False),
            default=Environment.DEV.value,
            help='Environment to run the command in.')

def cli(env: str) -> None:
    print(env)
    print(Environment.__members__.items())

@cli.command()
def test() -> None:
    print('test')


if __name__ == '__main__':
    cli()
