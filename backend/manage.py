import click

from cli.start import start


@click.group()
def main() -> None:
    """Administrative commands."""


main.add_command(start)


if __name__ == "__main__":
    main()
