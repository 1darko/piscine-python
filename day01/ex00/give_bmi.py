import numpy as np


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    Calculate BMI from height and weight lists.
    Returns a list of BMI values.
    """
    try:
        assert len(h) == len(w), "Lists must be of the same size."
        assert all(isinstance(h, (int, float)) for h in h) \
            or not h, "All height values must be int or float."
        assert all(isinstance(w, (int, float)) for w in w) \
            or not w, "All weight values must be int or float."
        np_height = np.array(h)
        np_weight = np.array(w)
        bmi = np_weight / (np_height ** 2)
        return bmi.tolist()
    except AssertionError as e:
        print(e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to the BMI list and return a list of booleans.
    True if BMI is above the limit, False otherwise.
    """
    try:
        assert limit and isinstance(limit, int), "Limit must be an integer."
        assert bmi and all(isinstance(b, (int, float)) for b in bmi), \
            "All BMI values must be int or float."
        np_bmi = np.array(bmi)
        result = np_bmi > limit
        return result.tolist()
    except AssertionError as e:
        print(e)
        return []
