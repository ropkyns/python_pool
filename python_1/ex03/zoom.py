from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(image:np.ndarray) -> np.ndarray:
    """Zoooooooooooooooooooooooom"""
    try:
        img_zoom = image[100:500, 450:850]
        print(f"New shape after slicing: {img_zoom.shape} or {img_zoom.squeeze().shape}")
        plt.imshow(img_zoom, cmap="gray")
        plt.show()
        return(img_zoom)
    except Exception as error:
        raise RuntimeError({error})


def main():
    try:
        img = ft_load("animal.jpeg")
        print(f"{img}\n")
        print(zoom(img))
    except KeyboardInterrupt:
        print("KeyboardInterrupt: a signal has been catched")
    except RuntimeError as error:
        print(error)


if __name__ == "__main__":
    main()