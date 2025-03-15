# YOLOv8 Image Detector

## Overview
The **YOLOv8 Image Detector** is a comprehensive Windows-based application designed to perform **object detection, segmentation, and pose estimation** using the **YOLOv8 model**. This project leverages **Deep Learning and Semantic Technologies** to enhance real-time detection efficiency and accuracy. 

### Key Features
- **Real-time Object Detection**: Utilizes YOLOv8 for accurate and efficient object recognition.
- **Segmentation & Pose Estimation**: Identifies object boundaries and human poses.
- **User-Friendly GUI**: Built with **PyQT** for seamless interaction.
- **Video & Image Processing**: Integrates **OpenCV** for enhanced media handling.

---

## Installation

Ensure you have all dependencies installed from the requirements.txt, which are subjetct to change and modernisation

### Steps to Install

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/yolov8-image-detector.git
   cd yolov8-image-detector
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```sh
   python -m venv yolov8_env
   source yolov8_env/bin/activate  # On Windows use yolov8_env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Download Pretrained YOLOv8 Model**:
   ```sh
   wget https://github.com/ultralytics/assets/releases/download/v8/yolov8n.pt  # or use curl
   ```

---

## Usage

1. **Run the Application**:
   ```sh
   python app.py
   ```
2. **Select an Input Source**:
   - Image file
   - Video file
   - Live webcam feed
3. **Adjust Model & Hyperparameters** via the PyQT interface.
4. **View Results** in real-time within the GUI.

---

## Acknowledgments
- **YOLOv8 by Ultralytics**
- **OpenCV for Image Processing**
- **PyQT for GUI Development**

---

## License
This project is licensed under the **MIT License**.

---

## Contact
For any questions or contributions, feel free to reach out or open an issue in this repository.
