import typer

hello_app = typer.Typer()


@hello_app.command()
def greet(name: str):
    """
    A command to greet someone by name.
    """
    print(f"Hello {name}!")
