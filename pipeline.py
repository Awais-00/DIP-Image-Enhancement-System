try:
    from .image_io import convert_to_gray
    from .intensity import gamma_correction
    from .histogram_ops import histogram_equalization
except ImportError:
    from image_io import convert_to_gray
    from intensity import gamma_correction
    from histogram_ops import histogram_equalization


def process_image(input_image):
    gray = convert_to_gray(input_image)

    # Best selected methods from previous phases:
    # 1. Gamma correction for brightening
    # 2. Histogram equalization for contrast improvement
    bright = gamma_correction(gray, 0.5)
    enhanced = histogram_equalization(bright)

    return enhanced
