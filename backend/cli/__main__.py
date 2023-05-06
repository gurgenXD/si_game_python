import click

from cli.migrations import migrations
from cli.start import start


@click.group()
def main() -> None:
    """Administrative commands."""


main.add_command(start)
main.add_command(migrations)


main()
