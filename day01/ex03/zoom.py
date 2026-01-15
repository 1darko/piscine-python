"""Create a program that should load the image "animal.jpeg", print some information
about it and display it after "zooming".
• The size in pixel on both X and Y axis
• The number of channel
• The pixel content of the image.
• Display the scale on the x and y axis on the image
If anything went wrong, the program must not stop abruptly and handle any error
with a clear message.
"""

import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from time import sleep
def zoom(scale_factor: float) -> np.ndarray | None:
    """Zooms an image represented as a NumPy array by a given scale factor.
    Args:
        np.ndarray: The input image as a NumPy array.
        scale_factor (float): The factor by which to zoom the image.
    """
    path ="/home/dakojic/Downloads/animal.jpeg"
    try:
        assert path and isinstance(path, str), "Path must be a non-empty string."
        assert path.endswith(('.jpg', '.jpeg')), \
            "Unsupported file format. Use .jpg or .jpeg files."
        assert scale_factor > 1, "Scale factor must be superior to 1."
        image = ft_load(path)
        assert image is not None, "Failed to load image."

        h, w = image.shape[:2]
        zoom_h = h / scale_factor
        zoom_w = w / scale_factor

        cy, cx = h // 2, w // 2

        yl = int(cy - zoom_h // 2)
        yr = int(cy + zoom_h // 2)
        xl = int(cx - zoom_w // 2)
        xr = int(cx + zoom_w // 2)

        cropped_image = image[yl:yr, xl:xr]
        # Set the image to grey if scale_factor is greater than or equal to 1.5
        if(scale_factor >= 1.5):
             cropped_image = cropped_image[:,:,0] * 0.299 + cropped_image[:,:,1] * 0.587 + cropped_image[:,:,2] * 0.114
        shape_info = cropped_image.shape[0], cropped_image.shape[1], cropped_image.shape[2] if len(cropped_image.shape) > 2 else 1
        print(f"New shape after slicing: {shape_info} or {cropped_image.shape}")        
        plt.imshow(cropped_image, cmap='grey' if scale_factor >= 1.5 else None)
        plt.show()
        return cropped_image
    # Handle ctrl + C interruption
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        return None
    except FileNotFoundError:
        print(f"Image file not found at path: {path}")
        return None
    except Exception as e:
        print(f"Error displaying image: {e}")
        return None
def main():
        zoom(3)

if __name__ == "__main__":
    main()