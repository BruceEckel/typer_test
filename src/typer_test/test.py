import typer

app = typer.Typer()


@app.command()
def subcommand_1():
    "Runs subcommand one"
    print("Running subcommand_1()")


@app.command()
def subcommand_2():
    "Runs subcommand two"
    print("Running subcommand_2()")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(typer.main.get_command(app).get_help(ctx))
        raise typer.Exit()


if __name__ == "__main__":
    app()
