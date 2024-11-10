import typer

goodbye_app = typer.Typer()

@goodbye_app.command()
def farewell(name: str, formal: bool = False):
    """
    A command to bid farewell to someone, with an optional formal mode.
    """
    if formal:
        print(f"Goodbye, Mr./Ms. {name}. Have a good day.")
    else:
        print(f"Bye, {name}!")