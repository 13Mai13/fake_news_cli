import typer
from commands import data_processing_app

app = typer.Typer()

# Adding each command as a subcommand to the main Typer app
# app.add_typer(hello_app, name="hello")
# app.add_typer(goodbye_app, name="goodbye")
app.add_typer(data_processing_app, name="extract_metadata")

if __name__ == "__main__":
    app()
