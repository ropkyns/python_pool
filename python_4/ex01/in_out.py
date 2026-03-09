def square(x: int | float) -> int | float:
    """function that return square of a number"""
    return x * x


def pow(x: int | float) -> int | float:
    """function that return power of a number by himself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """function that return an object that when called return\
 the argument calculation with the function given"""
    value = x

    def inner() -> float:
        nonlocal value
        value = function(value)
        return value
    return inner
