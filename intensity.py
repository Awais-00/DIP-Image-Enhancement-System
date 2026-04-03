import numpy as np
import cv2
import matplotlib.pyplot as plt


def negative_transform(gray_image):
    return 255 - gray_image


def log_transform(gray_image):
    img_float = gray_image.astype(np.float32)
    log_img = np.log1p(img_float)
    log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX)
    return log_img.astype(np.uint8)


def gamma_correction(gray_image, gamma):
    normalized = gray_image / 255.0
    corrected = np.power(normalized, gamma)
    corrected = (corrected * 255).astype(np.uint8)
    return corrected


def save_intensity_comparison(images_dict, save_path):
    plt.figure(figsize=(12, 6))
    for i, (title, img) in enumerate(images_dict.items(), start=1):
        plt.subplot(2, 3, i)
        plt.imshow(img, cmap="gray")
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()