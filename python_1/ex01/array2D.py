import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list), "1st arg is not a list"
    assert np.ndim(family) == 2, "List is not 2D"
    assert all(len(family[0]) is len(x) for x in family), "2nd dimensional list are not the same size"
    try:
        shape = np.shape(family)
        print(f"My shape is : {shape}")
        print(np.array(family))

    except AssertionError as error:
        print(f"AssertionError: {error}")