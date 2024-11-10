"""
All the commands related to data processing
"""
import typer

data_processing_app = typer.Typer()

@data_processing_app.command()
def extract_metadata(name: str = "all", path: str = ""):
    """
    A command to bid farewell to someone, with an optional formal mode.
    """
    if path & name:
        print(f"files {name} to path {path}")