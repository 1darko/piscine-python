def ft_filter(func, iterable):
    if func is None:
        return [items for items in iterable if items]
    else:
        return [items for items in iterable if func(items)]
