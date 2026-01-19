import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """
    Load an image from the given file path.
    Prints its format, and its pixels content in RGB format.
    Returns the image as a NumPy array or None if the file is not found.
    """
    try:
        assert path and isinstance(path, str), \
            "Path must be a non-empty string."
        assert path.endswith(('.jpg', '.jpeg')), \
            "Unsupported file format. Use .jpg or .jpeg files."
        image = plt.imread(path)
        print(f"Image shape: {image.shape}")
        print("Pixels content (RGB):")
        print(image)
        return image
    except FileNotFoundError:
        print(f"Image file not found at path: {path}")
        return None
    except AssertionError as e:
        print(e)
        return None
