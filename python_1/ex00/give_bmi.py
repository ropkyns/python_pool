import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Take two list one of height(s) and one of (weight) return list of bmi"""
    assert isinstance(height, list) and isinstance(weight, list), "Need list as args for this function"
    assert len(height) == len(weight), "Need list of the same size"
    assert all(isinstance(x, (int, float)) for x in height + weight), "Need list of integer or float"
    try:
        h = np.array(height)
        w = np.array(weight)
        return((w / (h * h)).tolist())
    except AssertionError as error:
        print(f"AssertionError: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """check if element of the list given as argument is above the limit or no return list of boolean"""
    assert isinstance(bmi, list) and type(limit) is int, "Need to give a list as first arg and integer for the second arg"
    assert all(isinstance(x, (int, float)) for x in bmi), "Need list of integer or float"
    return[x > limit for x in bmi]