import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def ensure_dirs(output_dir, results_dir):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)


def load_image(image_path):
    image_bgr = cv2.imread(image_path)
    if image_bgr is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    return image_bgr


def convert_to_rgb(image_bgr):
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)


def convert_to_gray(image_bgr):
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)


def save_image(path, image):
    cv2.imwrite(path, image)


def get_image_info(gray_image):
    height, width = gray_image.shape
    info = {
        "resolution": f"{width} x {height}",
        "dtype": str(gray_image.dtype),
        "partial_matrix": gray_image[:5, :5]
    }
    return info


def save_original_and_gray(rgb_image, gray_image, save_path):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(rgb_image)
    plt.title("Original RGB")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Grayscale")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()