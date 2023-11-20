#!/usr/bin/python3

def safe_function(fct, *args):
    """Executes a function safely."""

    from sys import stderr

    try:
        func_result = fct(*args)
        return (func_result)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return (None)
