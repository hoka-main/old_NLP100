def example_func(param1, param2):
    """example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): the second parameter.

    Returns:
        bool: The return value. Ture for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True
help(example_func)
print(example_func.__doc__)