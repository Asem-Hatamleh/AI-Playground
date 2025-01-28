# Advanced Night Vision System with Object Detection
# Aim
To develop an advanced night vision system that integrates object detection capabilities using AI and image processing techniques, enabling accurate recognition of objects in low-light or dark environments.

# Hypothesis
Real-time object detection can be effectively performed in low-light environments by employing advanced image enhancement techniques that enable the model to adapt to low lighting conditions.

# Materials
Camera for video capture: Used to record video streams in low-light conditions.

Gamma correction technique: Adjusts brightness to improve visibility in dark areas.

Gaussian denoising filter: Reduces noise in the image.

Roboflow dataset: A labeled dataset for training and testing the object detection model.

# Methodology
We applied three different image enhancement techniques to video captured from a camera stream in low-light conditions. Each method was tested to evaluate its impact on object detection performance using the YOLOv5 model.

# 1. No Enhancement
Description: Frames were captured directly from the video feed without any enhancements.

Results: Suboptimal object detection due to noisy and unclear images in low-light conditions.

# 2. Histogram Equalization
Description: Improved contrast by adjusting the intensity distribution of the image.

Results: Increased brightness but introduced significant noise, reducing detection accuracy.

# 3. Image Negatives
Description: Inverted pixel values to lighten dark areas.

Results: Brightened dark regions but created unnatural images, making object detection harder.

# 4. Gaussian Smoothing with Gamma Correction (Best Method)
Description: Combined Gaussian smoothing to reduce noise and gamma correction to adjust brightness.

Results: Significantly improved visibility in dark areas and reduced noise, leading to higher object detection accuracy.

# Results
No Enhancement: Limited detection capabilities with low precision and recall.

Histogram Equalization: Improved contrast but introduced excessive noise.

Image Negatives: Brightened dark regions but created unnatural images.

Gaussian Smoothing with Gamma Correction: Achieved the highest precision and recall, with improved mean Average Precision (mAP).

# Discussion
# 1. Is the hypothesis supported or disproved?
The hypothesis is supported. Gaussian smoothing with gamma correction proved to be the most effective method for improving object detection in low-light conditions.

# 2. What problems were encountered?
Increased noise with histogram equalization.

Unnatural image appearance with image negatives.

Real-time processing delays due to smoothing techniques.

# 3. How could the experiment be improved?
Testing advanced techniques like adaptive histogram equalization or deep learning-based enhancement.

Dynamically adjusting enhancement parameters based on lighting conditions.

Experimenting with other object detection models for better performance.

# Conclusion
Gaussian smoothing with gamma correction was identified as the most effective method for enhancing object detection accuracy in low-light conditions. This technique reduced noise and improved visibility in dark areas, making it suitable for real-time applications. 

# Code

Click [here](https://github.com/TF-Hatamleh/DIP/blob/main/DIP.ipynb) to access the code for this project.


 
 
