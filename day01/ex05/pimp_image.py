from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(img: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the image.
    """
    try:
        assert img.ndim == 3 and img.shape[2] >= 3, "Image must be RGB"
        inverted = img.copy().astype(float)
        inverted[:, :, 0] = 255 - inverted[:, :, 0]
        inverted[:, :, 1] = 255 - inverted[:, :, 1]
        inverted[:, :, 2] = 255 - inverted[:, :, 2]
        inverted = np.clip(inverted, 0, 255).astype(np.uint8)
    except AssertionError as e:
        print(f"Error in ft_invert: {e}")
        return img
    plt.imshow(inverted)
    plt.axis("off")
    plt.title("Inverted Image")
    plt.show()
    return inverted


def ft_red(img: np.ndarray) -> np.ndarray:
    """
    Set the image to red colors.
    """
    try:
        assert img.ndim == 3 and img.shape[2] >= 3, "Image must be RGB"
        red_img = img.copy().astype(float)
        #red_img[:, :, 0] *= 2
        red_img[:, :, 1] *= 0.2
        red_img[:, :, 2] *= 0.2
        red_img = np.clip(red_img, 0, 255).astype(np.uint8)
    except AssertionError as e:
        print(f"Error in ft_red: {e}")
        return None
    plt.imshow(red_img)
    plt.axis("off")
    plt.title("Red Image")
    plt.show()
    return red_img

def ft_green(img: np.ndarray) -> np.ndarray | None:
    """ 
    Set the image to green colors.
    """
    try:
        assert img.ndim == 3 and img.shape[2] >= 3, "Image must be RGB"
        green_img = img.copy().astype(float)
        green_img[:, :, 0] = 10
        #green_img[:, :, 1] *= 0.2
        green_img[:, :, 2] = 10
        green_img = np.clip(green_img, 0, 255).astype(np.uint8)
    except AssertionError as e:
        print(f"Error in ft_green: {e}")
        return None
    plt.imshow(green_img)
    plt.axis("off")
    plt.title("Green Image")
    plt.show()
    return green_img

def ft_blue(img: np.ndarray) -> np.ndarray:
    """ 
    Set the image to blue colors.
    """
    try:
        assert img.ndim == 3 and img.shape[2] >= 3, "Image must be RGB"
        blue_image = img.copy().astype(float)
        blue_image[:, :, 0] = 10
        blue_image[:, :, 1] = 10
        #blue_image[:, :, 2] /= 2
        blue_image = np.clip(blue_image, 0, 255).astype(np.uint8)
    except AssertionError as e:
        print(f"Error in ft_blue: {e}")
        return None
    plt.imshow(blue_image)
    plt.axis("off")
    plt.title("Blue Image")
    plt.show()
    return blue_image


def ft_grey(img: np.ndarray) -> np.ndarray:
    """
    Set the image to grey colors.
    """
    try:
        assert img.ndim == 3 and img.shape[2] >= 3, "Image must be RGB"

        grey_image = img.copy().astype(float)
        grey_image = (
            grey_image[:, :, 0] / (1/0.299) +
            grey_image[:, :, 1] / (1/0.587) +
            grey_image[:, :, 2] / (1/0.114)
        )
        grey_rgb = np.stack([grey_image, grey_image, grey_image], axis=2)
        grey_rgb = np.clip(grey_rgb, 0, 255).astype(np.uint8)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        return None
    except AssertionError as e:
        print(f"Error in ft_grey: {e}")
        return None

    plt.imshow(grey_rgb, cmap='gray')
    plt.axis("off")
    plt.title("Grey Image")
    plt.show()
    return grey_rgb

def main():
    path ="/home/dakojic/Downloads/landscape.jpg"
    image = ft_load(path)
    try:
        assert image is not None, "Failed to load image."
        ft_invert(image)
        ft_grey(image)
        ft_red(image)
        ft_blue(image)
        ft_green(image)
        print(ft_invert.__doc__)
        print(ft_grey.__doc__)
        print(ft_red.__doc__)
        print(ft_blue.__doc__)
        print(ft_green.__doc__)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        exit(1)
    except Exception as e:
        print(f"Error processing image: {e}")
if __name__ == "__main__":
    main()



