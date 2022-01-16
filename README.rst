Example
=======

Run the following in this directory::

    > python -m venv venv
    > ./venv/bin/pip install -e .
    > ./venv/bin/pip install mypy pylama

Then mypy reveals correct types::

    > ./venv/bin/mypy confusion
    confusion/contains_something/things.py:8: note: Revealed type is "def (value: builtins.str) -> confusion.contains_something.things.Something"
    confusion/uses_something/uses.py:3: note: Revealed type is "def (value: builtins.str) -> confusion.contains_something.things.Something"

But pylama does not::

    > ./venv/bin/pylama
    confusion/contains_something/things.py:8:13  Revealed type is "def (value: builtins.str) -> confusion.contains_something.things.Something" [mypy]
    confusion/uses_something/uses.py:3:13  Revealed type is "Any" [mypy]


And if I edit the pylama mypy plugin to not have the '--follow-imports=skip' option in
``venv/lib/python3.10/site-packages/pylama/lint/pylama_mypy.py:21`` then I get::

    > ./venv/bin/pylama
    confusion/contains_something/things.py:8:13  Revealed type is "def (value: builtins.str) -> confusion.contains_something.things.Something" [mypy]
    confusion/uses_something/uses.py:3:13  Revealed type is "def (value: builtins.str) -> confusion.contains_something.things.Something" [mypy]
