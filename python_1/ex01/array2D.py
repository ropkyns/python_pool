import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of the array given as argument and returned
    the truncanated version based on the provided start and end arguments"""
    assert isinstance(family, list), "1st arg is not a list"
    assert np.ndim(family) == 2, "List is not 2D"
    assert all(len(family[0]) is len(x) for x in family), "2nd dimensional \
        list are not the same size"
    try:
        print(f"My shape is : {np.shape(family)}")
        new_shape = family[start:end]
        print(f"My new shape is : {np.shape(new_shape)}")
        return (new_shape)

    except AssertionError as error:
        print(f"AssertionError: {error}")
