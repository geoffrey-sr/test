# broken_test.py


def foo(a, b):
    print(a + b)  # whitespace around arguments (ruff: E203)


def bar():
    x = 1  # wrong indentation (ruff: E111)
    y = 2
    return x + y  # missing whitespace (ruff: E231)


foo(1, 2)
bar()  # semicolon usage (ruff: E703)

unused_var = 123  # unused variable (ruff: F841)
