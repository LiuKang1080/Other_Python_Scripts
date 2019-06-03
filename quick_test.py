def func_name(function):
    return function.__name__


@len
@func_name
def nineteen_characters():
    """19 characters are in this function's name"""
    pass


print(nineteen_characters)
