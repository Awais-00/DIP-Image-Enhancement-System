# Smart Image Enhancement & Analysis System

## Overview
This project was developed as part of a Digital Image Processing lab to design a complete image enhancement application. The system takes a low-quality image as input and applies a series of image processing techniques to improve its visual quality.

## Objective
The objective of this project is to analyze and enhance images by implementing fundamental digital image processing operations, and to integrate them into a complete working pipeline.

## Technologies Used
- Python
- OpenCV
- NumPy
- Matplotlib

## Project Structure
DIP-Image-Enhancement-System/
- code/
- images/input/
- images/output/
- results/
- README.md
- report.pdf

## Features Implemented

### 1. Image Acquisition & Understanding
- Image loading
- RGB to grayscale conversion
- Resolution, data type, and matrix analysis

### 2. Sampling & Quantization
- Image resizing (0.25x, 0.5x, 1.5x, 2x)
- Bit-depth reduction (8-bit, 4-bit, 2-bit)
- Quality comparison and degradation analysis

### 3. Geometric Transformations
- Rotation (multiple angles)
- Translation
- Shearing
- Inverse transformations for restoration

### 4. Intensity Transformations
- Negative transformation
- Log transformation
- Gamma correction (γ = 0.5, 1.5)

### 5. Histogram Processing
- Histogram visualization
- Histogram equalization
- Contrast enhancement

### 6. Final Enhancement Pipeline
The final system integrates:
- Grayscale conversion
- Gamma correction (γ = 0.5)
- Histogram equalization

## Results
The system successfully enhances low-quality images by improving brightness, contrast, and overall visual clarity. Comparative results and visual outputs are included in the `results/` directory.

## Key Learnings
- Impact of sampling and quantization on image quality
- Importance of intensity transformations in enhancement
- Role of histogram equalization in contrast improvement
- Designing a modular and scalable image processing pipeline

## How to Run
```bash
cd code
python main.py
