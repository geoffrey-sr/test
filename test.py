# broken_test.py

import os

print(os.name)  # use os somewhere


def foo(a, b):
    print(a + b)  # whitespace around arguments (ruff: E203)


def bar():
    x = 1
    y = 2
    return x + y


foo(1, 2)
bar()
unused_var = 123  # unused variable (ruff: F841)
