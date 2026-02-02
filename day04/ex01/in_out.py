def square(x: int | float) -> int | float:
    #your code here
    try:
        assert isinstance(x, (int, float))
    except AssertionError:
        print("Input must be an integer or float")
        return None
    return x * x

def pow(x: int | float) -> int | float:
    #your code here
    try:
        assert isinstance(x, (int, float))
    except AssertionError:
        print("Input must be an integer or float")
        return None
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    value = x
    def inner() -> float:
        nonlocal value, count
        count += 1
        value = function(value)
        return value
    return inner