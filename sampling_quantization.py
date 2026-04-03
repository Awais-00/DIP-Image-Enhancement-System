import cv2
import matplotlib.pyplot as plt


def resize_image(gray_image, scale):
    height, width = gray_image.shape
    new_width = max(1, int(width * scale))
    new_height = max(1, int(height * scale))
    resized = cv2.resize(gray_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    return resized


def reduce_bit_depth(gray_image, bits):
    levels = 2 ** bits
    factor = 256 // levels
    reduced = (gray_image // factor) * factor
    return reduced.astype("uint8")


def save_sampling_comparison(images_dict, save_path):
    plt.figure(figsize=(12, 8))
    for i, (title, img) in enumerate(images_dict.items(), start=1):
        plt.subplot(2, 3, i)
        plt.imshow(img, cmap="gray")
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def save_quantization_comparison(images_dict, save_path):
    plt.figure(figsize=(10, 4))
    for i, (title, img) in enumerate(images_dict.items(), start=1):
        plt.subplot(1, 3, i)
        plt.imshow(img, cmap="gray")
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()