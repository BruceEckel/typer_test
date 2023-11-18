# typer_test
Demonstrates a problem with typer.

The application automatically produces help when run using the Python command line (with no arguments):

```
> python foo.py
```

Notice that the user doesn't have to add `--help` in order to produce help.

The problem occurs when the app is installed using `pip`. 
Do this by opening a command prompt in the base directory of the cloned repository, then running:

```
> pip install -e .
```

Because of the following configuration in the `pyproject.toml` file:

```toml

```

The `pip` command above installs the `test1` program so you can run `foo.py` with the simple command:

```
> test1
```

However, running `test1` this way produces the following error message:
