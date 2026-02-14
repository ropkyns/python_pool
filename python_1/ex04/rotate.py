from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom_transpose(image: np.ndarray) -> np.ndarray:
    """Zoooooooooooooooooooooooom"""
    try:
        img_zoom = image[100:500, 450:850]
        img_gray = img_zoom.mean(axis=2)
        output = img_gray[:, :, None]
        print(f"The shape of image is: {output.shape}", end="")
        print(f" or {output.squeeze().shape}")
        print(f"{output}\n")
        output = np.transpose(output, (1, 0, 2))
        print(f"New shape after transpose : {output.squeeze().shape}")
        plt.imshow(output, cmap="gray")
        plt.show()
        return (output)
    except Exception as error:
        raise RuntimeError({error})


def main():
    try:
        img = ft_load("animal.jpeg")
        print(zoom_transpose(img))
    except KeyboardInterrupt:
        print("KeyboardInterrupt: a signal has been catched")
    except RuntimeError as error:
        print(error)


if __name__ == "__main__":
    main()
