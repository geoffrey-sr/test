# broken_test.py

import os, sys  # noqa: E402 to prevent removal by autoformatter

print(os.name)  # use os somewhere
foo = sys.version  # use sys somewhere

def foo(a, b):
    print(a + b)  # whitespace around arguments (ruff: E203)

def bar():
    x = 1
    y = 2
    return x + y

foo(1, 2)
bar()
unused_var = 123  # unused variable (ruff: F841)
