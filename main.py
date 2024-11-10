import typer
from commands import hello_app, goodbye_app

app = typer.Typer()

# Adding each command as a subcommand to the main Typer app
app.add_typer(hello_app, name="hello")
app.add_typer(goodbye_app, name="goodbye")

if __name__ == "__main__":
    app()
