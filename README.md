# typer_test
Demonstrates a problem with typer.

The application automatically produces help when run using the Python command line (with no arguments):

```
PS C:\git\typer_test> python .\src\typer_test\test.py

 Usage: test.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.       │
│ --help                        Show this message and exit.                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ subcommand-1                                   Runs subcommand one                                                   │
│ subcommand-2                                   Runs subcommand two                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Notice that the user doesn't have to add `--help` in order to produce help.

The problem occurs when the app is installed using `pip`. 
Do this by opening a command prompt in the base directory of the cloned repository, then running:

```
> pip install -e .
```

Because of the following configuration in the `pyproject.toml` file:

```toml
[project.scripts]
test1 = "typer_test.test:main"
```

The `pip` command above installs the `test1` program so you can run `foo.py` with the simple command:

```
> test1
```

However, running `test1` this way produces the following error message:

```
PS C:\git\typer_test> test1
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Python\Scripts\test1.exe\__main__.py", line 7, in <module>
TypeError: main() missing 1 required positional argument: 'ctx'
```
