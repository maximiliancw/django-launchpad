# django_launchpad/cli.py
import click


@click.group()
def cli():
    """CLI for django-launchpad"""
    pass

@cli.command()
@click.argument("config_file", type=click.Path(exists=True))
@click.option("--app-name", prompt="App name", help="Name of the Django app to generate.")
@click.option("--output-dir", default=".", help="Directory where the app should be created.")
def generate(config_file, app_name, output_dir):
    """Generate Django app based on JSON or YAML configuration file."""
    click.echo(f"Reading configuration from {config_file}")
    click.echo(f"Generating Django app '{app_name}' in {output_dir}")

    # Placeholder for future functionality
    # This is where we’ll load the config file and generate app files

if __name__ == "__main__":
    cli()
