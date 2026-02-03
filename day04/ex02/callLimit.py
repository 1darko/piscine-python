from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Inner decorator function."""
        def limit_function(*args: Any, **kwds: Any):
            """Wrapper function that enforces the call limit."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Function {function} call too many times")
                return None
        return limit_function
    return callLimiter

# @callLimit(3)
# def f():
#     print("f()")
# @callLimit(1)
# def g():
#     print ("g()")
# for i in range(3):
#     f()
#     g()
