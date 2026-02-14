import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Invert the color of the image received"""
    try:
        res = 255 - array
        plt.imshow(res)
        plt.axis("off")
        plt.show()
        return res
    except Exception as error:
        raise RuntimeError(f"image invertion failed: {error}")


def ft_red(array) -> np.ndarray:
    """Show the image with a red filter"""
    try:
        res = array.copy()
        res[:, :, 1] = 0
        res[:, :, 2] = 0
        plt.imshow(res)
        plt.axis("off")
        plt.show()
        return res
    except Exception as error:
        raise RuntimeError(f"filter application on image failed: {error}")


def ft_green(array) -> np.ndarray:
    """Show the image with a green filter"""
    try:
        res = array.copy()
        res[:, :, 0] = 0
        res[:, :, 2] = 0
        plt.imshow(res)
        plt.axis("off")
        plt.show()
        return res
    except Exception as error:
        raise RuntimeError(f"filter application on image failed: {error}")


def ft_blue(array) -> np.ndarray:
    """Show the image with a blue filter"""
    try:
        res = array.copy()
        res[:, :, 0] = 0
        res[:, :, 1] = 0
        plt.imshow(res)
        plt.axis("off")
        plt.show()
        return res
    except Exception as error:
        raise RuntimeError(f"filter application on image failed: {error}")


def ft_grey(array) -> np.ndarray:
    """Show the image with a grey filter"""
    try:
        cpy = array.copy()
        res = cpy.mean(axis=2)
        output = res[:, :, None]
        plt.imshow(output, cmap="gray")
        plt.axis("off")
        plt.show()
        return res
    except Exception as error:
        raise RuntimeError(f"filter application on image failed: {error}")
