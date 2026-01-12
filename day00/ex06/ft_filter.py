def ft_filter(func, iterable):
    """
    Filters elements from the iterable based on the provided function.
    If func is None, removes all elements that are considered False.
    """
    if func is None:
        return [items for items in iterable if items]
    else:
        return [items for items in iterable if func(items)]
