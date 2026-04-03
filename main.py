import os

try:
    from functions.image_io import (
        ensure_dirs,
        load_image,
        convert_to_rgb,
        convert_to_gray,
        save_image,
        get_image_info,
        save_original_and_gray
    )

    from functions.sampling_quantization import (
        resize_image,
        reduce_bit_depth,
        save_sampling_comparison,
        save_quantization_comparison
    )

    from functions.transformations import (
        rotate_image,
        translate_image,
        shear_image,
        inverse_rotate,
        inverse_translate,
        save_transformations_grid
    )

    from functions.intensity import (
        negative_transform,
        log_transform,
        gamma_correction,
        save_intensity_comparison
    )

    from functions.histogram_ops import (
        histogram_equalization,
        save_histogram,
        save_before_after_images,
        save_before_after_histograms
    )

    from functions.pipeline import process_image
except ModuleNotFoundError:
    # Support running as a direct script from code/functions.
    from image_io import (
        ensure_dirs,
        load_image,
        convert_to_rgb,
        convert_to_gray,
        save_image,
        get_image_info,
        save_original_and_gray
    )

    from sampling_quantization import (
        resize_image,
        reduce_bit_depth,
        save_sampling_comparison,
        save_quantization_comparison
    )

    from transformations import (
        rotate_image,
        translate_image,
        shear_image,
        inverse_rotate,
        inverse_translate,
        save_transformations_grid
    )

    from intensity import (
        negative_transform,
        log_transform,
        gamma_correction,
        save_intensity_comparison
    )

    from histogram_ops import (
        histogram_equalization,
        save_histogram,
        save_before_after_images,
        save_before_after_histograms
    )

    from pipeline import process_image


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    input_path = os.path.join(base_dir, "images", "input", "input.jpg")
    output_dir = os.path.join(base_dir, "images", "output")
    results_dir = os.path.join(base_dir, "results")

    ensure_dirs(output_dir, results_dir)

    # =========================
    # 6.1 Image Acquisition & Understanding
    # =========================
    image_bgr = load_image(input_path)
    image_rgb = convert_to_rgb(image_bgr)
    gray = convert_to_gray(image_bgr)

    save_image(os.path.join(output_dir, "grayscale.jpg"), gray)
    save_original_and_gray(
        image_rgb,
        gray,
        os.path.join(results_dir, "01_original_and_grayscale.png")
    )

    info = get_image_info(gray)
    print("\n=== IMAGE REPORT ===")
    print("Resolution:", info["resolution"])
    print("Data Type:", info["dtype"])
    print("Partial Matrix (5x5):")
    print(info["partial_matrix"])

    # =========================
    # 6.2 Sampling & Quantization
    # =========================
    scales = [0.25, 0.5, 1.0, 1.5, 2.0]
    sampled_images = {}

    for scale in scales:
        img = resize_image(gray, scale)
        sampled_images[f"Scale {scale}"] = img
        filename = f"sampled_{str(scale).replace('.', '_')}.jpg"
        save_image(os.path.join(output_dir, filename), img)

    save_sampling_comparison(
        sampled_images,
        os.path.join(results_dir, "02_sampling_comparison.png")
    )

    bit_depth_images = {
        "8-bit": reduce_bit_depth(gray, 8),
        "4-bit": reduce_bit_depth(gray, 4),
        "2-bit": reduce_bit_depth(gray, 2)
    }

    for title, img in bit_depth_images.items():
        filename = title.lower().replace("-", "_") + ".jpg"
        save_image(os.path.join(output_dir, filename), img)

    save_quantization_comparison(
        bit_depth_images,
        os.path.join(results_dir, "03_quantization_comparison.png")
    )

    # =========================
    # 6.3 Geometric Transformations
    # =========================
    transform_images = {"Original": gray}

    angles = [30, 45, 60, 90, 120, 150, 180]
    rotated_45 = None

    for angle in angles:
        rotated, _ = rotate_image(gray, angle)
        transform_images[f"Rot {angle}"] = rotated
        save_image(os.path.join(output_dir, f"rotated_{angle}.jpg"), rotated)
        if angle == 45:
            rotated_45 = rotated

    translated, _ = translate_image(gray, 50, 30)
    sheared, _ = shear_image(gray, 0.3)

    save_image(os.path.join(output_dir, "translated.jpg"), translated)
    save_image(os.path.join(output_dir, "sheared.jpg"), sheared)

    restored_rot = inverse_rotate(rotated_45, 45)
    restored_trans = inverse_translate(translated, 50, 30)

    save_image(os.path.join(output_dir, "restored_rotation.jpg"), restored_rot)
    save_image(os.path.join(output_dir, "restored_translation.jpg"), restored_trans)

    transform_images["Translated"] = translated
    transform_images["Sheared"] = sheared
    transform_images["Restored Rot"] = restored_rot
    transform_images["Restored Trans"] = restored_trans

    save_transformations_grid(
        transform_images,
        os.path.join(results_dir, "04_transformations.png")
    )

    # =========================
    # 6.4 Intensity Transformations
    # =========================
    negative = negative_transform(gray)
    log_img = log_transform(gray)
    gamma_05 = gamma_correction(gray, 0.5)
    gamma_15 = gamma_correction(gray, 1.5)

    save_image(os.path.join(output_dir, "negative.jpg"), negative)
    save_image(os.path.join(output_dir, "log_transform.jpg"), log_img)
    save_image(os.path.join(output_dir, "gamma_0_5.jpg"), gamma_05)
    save_image(os.path.join(output_dir, "gamma_1_5.jpg"), gamma_15)

    intensity_images = {
        "Original": gray,
        "Negative": negative,
        "Log": log_img,
        "Gamma 0.5": gamma_05,
        "Gamma 1.5": gamma_15
    }

    save_intensity_comparison(
        intensity_images,
        os.path.join(results_dir, "05_intensity_comparison.png")
    )

    # =========================
    # 6.5 Histogram Processing
    # =========================
    equalized = histogram_equalization(gray)

    save_image(os.path.join(output_dir, "equalized.jpg"), equalized)

    save_histogram(
        gray,
        "Original Histogram",
        os.path.join(results_dir, "06_original_histogram.png")
    )

    save_before_after_images(
        gray,
        equalized,
        os.path.join(results_dir, "07_before_after_equalization.png")
    )

    save_before_after_histograms(
        gray,
        equalized,
        os.path.join(results_dir, "08_before_after_histograms.png")
    )

    # =========================
    # 6.6 Final Integrated System
    # =========================
    final_output = process_image(image_bgr)
    save_image(os.path.join(output_dir, "final_enhanced.jpg"), final_output)

    save_before_after_images(
        gray,
        final_output,
        os.path.join(results_dir, "09_final_pipeline_result.png")
    )

    print("\n=== FINAL PIPELINE COMPLETE ===")
    print("All output images saved in: images/output/")
    print("All result visuals saved in: results/")


if __name__ == "__main__":
    main()
