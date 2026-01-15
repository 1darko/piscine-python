from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

def rotate() -> np.ndarray | None :
    """Rotate an image represented as a NumPy array by 90 degrees.
    Args:
        np.ndarray: The input image as a NumPy array.
    """
    path ="/home/dakojic/Downloads/animal.jpeg"
    try:
        assert path and isinstance(path, str), "Path must be a non-empty string."
        assert path.endswith(('.jpg', '.jpeg')), \
            "Unsupported file format. Use .jpg or .jpeg files."
        image = ft_load(path)
        assert image is not None, "Failed to load image."

        h, w = image.shape[:2]
        cy, cx = h // 2, w // 2
        scale = 400
        yl = int(cy - scale // 2)
        yr = int(cy + scale // 2)
        xl = int(cx - scale // 2)
        xr = int(cx + scale // 2)

        cropped_image = image[yl:yr, xl:xr]
        # Set the image to grey if scale_factor is greater than or equal to 1.5
        cropped_image = cropped_image[:,:,0] * 0.299 + cropped_image[:,:,1] * 0.587 + cropped_image[:,:,2] * 0.114
        shape_info = cropped_image.shape[0], cropped_image.shape[1], 1
        rotated_image = np.empty((scale, scale), dtype=cropped_image.dtype)
        for x in range(scale):
            for y in range(scale):
                rotated_image[scale - 1 - y, x] = cropped_image[x,y]
        plt.imshow(rotated_image, cmap='grey')
        print(f'New shape after Transpose: {rotated_image.shape}')
        print(rotated_image)
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
    rotate()

if __name__ == "__main__":
    main()