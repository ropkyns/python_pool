import os
import numpy as np
import matplotlib.image as mimg


def ft_load(path: str) -> np.ndarray:
    """Load image given as argument and print it's shape"""
    assert os.path.exists, "file does not exist"
    assert path.endswith(".jpg") or path.endswith(".jpeg"), "Need to turn in an image .jpg or jpeg"
    try:
        img = mimg.imread(path)
        print(f"The shape of image is: {img.shape}")
    except Exception as error:
        raise RuntimeError(f"Failed to read image: {error}")
    return(img)