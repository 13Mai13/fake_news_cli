"""
All the commands and their options are configured here
"""
import typer
from typing import List

app = typer.Typer()

@app.command()
def yourcommand(files: List[str], name: str = None):
    if name:
        print(f"Hello {name}")
    print(files)