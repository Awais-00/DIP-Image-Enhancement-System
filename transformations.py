import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate_image(gray_image, angle):
    height, width = gray_image.shape
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray_image, matrix, (width, height))
    return rotated, matrix


def translate_image(gray_image, tx, ty):
    height, width = gray_image.shape
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated = cv2.warpAffine(gray_image, matrix, (width, height))
    return translated, matrix


def shear_image(gray_image, shear_factor=0.3):
    height, width = gray_image.shape
    matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    sheared = cv2.warpAffine(gray_image, matrix, (width, height))
    return sheared, matrix


def inverse_rotate(gray_image, angle):
    restored, _ = rotate_image(gray_image, -angle)
    return restored


def inverse_translate(gray_image, tx, ty):
    restored, _ = translate_image(gray_image, -tx, -ty)
    return restored


def save_transformations_grid(images_dict, save_path):
    plt.figure(figsize=(14, 8))
    for i, (title, img) in enumerate(images_dict.items(), start=1):
        plt.subplot(3, 4, i)
        plt.imshow(img, cmap="gray")
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()