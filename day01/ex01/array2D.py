def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (family) from start index to end index.
    Returns the sliced portion as a list.
    """
    try:
        assert isinstance(start, int), "Start must be an integer."
        assert isinstance(end, int), "End must be an integer."
        assert isinstance(family, list), "Family must be a list."
        return family[start:end]
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
