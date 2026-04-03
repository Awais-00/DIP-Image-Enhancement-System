import cv2
import matplotlib.pyplot as plt


def histogram_equalization(gray_image):
    return cv2.equalizeHist(gray_image)


def save_histogram(gray_image, title, save_path):
    plt.figure(figsize=(8, 4))
    plt.hist(gray_image.ravel(), bins=256, range=[0, 256])
    plt.title(title)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def save_before_after_images(original, enhanced, save_path):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(enhanced, cmap="gray")
    plt.title("Histogram Equalized")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def save_before_after_histograms(original, enhanced, save_path):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.hist(original.ravel(), bins=256, range=[0, 256])
    plt.title("Original Histogram")

    plt.subplot(1, 2, 2)
    plt.hist(enhanced.ravel(), bins=256, range=[0, 256])
    plt.title("Equalized Histogram")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()