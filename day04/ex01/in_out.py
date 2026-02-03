def square(x: int | float) -> int | float:
    """Returns the square of x."""
    try:
        assert isinstance(x, (int, float))
    except AssertionError:
        print("Input must be an integer or float")
        return None
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    try:
        assert isinstance(x, (int, float))
    except AssertionError:
        print("Input must be an integer or float")
        return None
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a closure that applies
    'function' to 'x' each time it is called."""
    count = 0
    value = x

    def inner() -> float:
        nonlocal value, count
        count += 1
        value = function(value)
        return value
    return inner
