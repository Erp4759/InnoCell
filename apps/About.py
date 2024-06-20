import streamlit as st


def app():
    st.title("About the Cervical Cancer Detection Project")

    st.write("""
    ## Project Overview

    This project aims to enhance the early detection and diagnosis of cervical cancer using advanced deep learning techniques. By utilizing YOLOv9, a highly efficient object detection model, we can accurately identify and classify cervical cancer cells in medical images.
    """)

    st.header("YOLOv9 Architecture")

    st.subheader("1. Backbone: Efficient Feature Extraction")
    st.write("""
    - **Purpose:** Extracts important features from the input image to understand the objects present and their locations.
    - **How It Works:** Uses a convolutional neural network (CNN) like EfficientNet to process the input image through multiple layers, capturing features such as edges, textures, and shapes.
    - **Feature Maps:** Transforms the image into a set of feature maps that highlight areas of interest.
    """)

    st.subheader("2. Neck: Feature Aggregation")
    st.write("""
    - **Purpose:** Processes feature maps from the backbone to enhance detection of objects at different scales.
    - **How It Works:** Uses a Feature Pyramid Network (FPN) and Path Aggregation Network (PAN) to merge features from various backbone layers, allowing for effective detection of small and large objects.
    - **Refined Features:** Outputs refined feature maps that are passed to the head for final processing.
    """)

    st.subheader("3. Head: Object Detection and Classification")
    st.write("""
    - **Purpose:** Generates the final predictions, including the location and class of each detected object.
    - **How It Works:** Processes the refined feature maps from the neck, predicting bounding boxes and class probabilities, and outputs the final detection results.
    - **Flexibility:** Designed to be flexible and dynamic, adapting to different object scales and aspect ratios.
    """)

    st.header("Performance Metrics")

    st.subheader("1. Precision")
    st.write("""
    - **Definition:** Measures the accuracy of the detected items by determining how many of the identified items are relevant.
    - **Importance:** High precision is crucial in medical diagnostics to ensure that detected cancer cells are indeed cancerous, minimizing false alarms.
    """)

    st.subheader("2. Average Precision")
    st.write("""
    - **Definition:** Calculated for each class individually by computing precision at different levels of recall.
    - **Precision-Recall Curve:** The area under the precision-recall curve represents the Average Precision.
    - **Importance:** Provides a detailed measure of performance for each class.
    """)

    st.subheader("3. Mean Average Precision (mAP)")
    st.write("""
    - **Definition:** The average of the Average Precision values across all classes, providing an overall measure of detection performance.
    - **Importance:** mAP is a comprehensive metric that reflects the model’s ability to detect and classify objects accurately.
    """)

    st.header("Advanced Features in YOLOv9")

    st.subheader("Attention Mechanisms")
    st.write("""
    - **Purpose:** Helps the model focus on important parts of the image, improving accuracy in detecting objects in cluttered or complex scenes.
    - **Example:** In a microscopic image where cancer cells overlap, the spatial attention mechanism can effectively highlight and differentiate individual cells.
    """)

    st.subheader("Enhanced Data Augmentation")
    st.write("""
    - **Techniques:** Uses strategies like Mosaic and Mixup during training to improve model robustness to variations in input data.
    - **Example:** Simulating cell overlaps or varying lighting and contrast conditions, helping the model learn to classify cells under diverse conditions.
    """)

    st.subheader("Improved Post-Processing")
    st.write("""
    - **Techniques:** Employs methods like Soft-NMS to reduce overlapping bounding boxes, ensuring that each object is detected only once.
    - **Importance:** Reduces false positives and improves the precision of detection.
    """)

    st.subheader("Dynamic Head Structure")
    st.write("""
    - **Purpose:** Adapts dynamically to different object scales and aspect ratios.
    - **Importance:** Enhances the model’s versatility and performance in various detection scenarios.
    """)

    st.header("Why YOLOv9 Stands Out")

    st.subheader("Advanced Architecture")
    st.write("""
    - **Importance:** Builds upon previous YOLO models with enhancements that improve both precision and recall.
    - **Example:** For cancer cells, where precise boundaries and characteristics are crucial, YOLOv9's refined architecture allows it to detect and classify cells more accurately.
    """)

    st.subheader("Improved Spatial Attention Mechanisms")
    st.write("""
    - **Importance:** Helps the model distinguish between overlapping objects.
    - **Example:** In a microscopic image with overlapping cancer cells, the spatial attention mechanism can highlight and differentiate individual cells.
    """)

    st.subheader("Better Handling of Small Objects and Complex Backgrounds")
    st.write("""
    - **Importance:** Ensures accurate detection and classification of small cancer cells even in complex backgrounds.
    - **Example:** Detecting small cells surrounded by various tissues, which is crucial for reliable diagnosis.
    """)

    st.subheader("Faster Inference and Efficient Computation")
    st.write("""
    - **Importance:** Allows for quicker processing times without sacrificing accuracy.
    - **Example:** Faster diagnosis and treatment planning, which is critical for timely cancer interventions.
    """)

    st.subheader("Robust Data Augmentation Techniques")
    st.write("""
    - **Importance:** Improves the model’s generalization by exposing it to diverse scenarios during training.
    - **Example:** Simulating different lighting conditions or object orientations, helping the model accurately classify cells under various conditions.
    """)

    st.write("""
    These features collectively make YOLOv9 a powerful tool for cervical cancer cell classification, particularly in challenging scenarios where cells may overlap or be difficult to distinguish due to their small size and complex environments.
    """)
