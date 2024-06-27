# Vehicle Detection and Classification using YOLOv8

This project implements vehicle detection and classification using the YOLOv8 model. The code processes a video, detects vehicles, tracks their movements, and counts the number of vehicles that cross a specified line in the video.

## How It Works

1. **Model Initialization**: The YOLOv8 model is loaded using the `YOLO` class from the `ultralytics` package.
2. **Video Capture**: The input video is read frame by frame using OpenCV.
3. **Line Definition**: A line is defined across which vehicle crossings are detected.
4. **Tracking and Detection**: Vehicles are detected and tracked across frames using the YOLOv8 model.
5. **Counting Crossings**: The code counts how many vehicles cross the defined line.
6. **Video Annotation**: The video frames are annotated with bounding boxes around detected vehicles and the count of vehicles that crossed the line.
7. **Output Video**: An output video with these annotations is saved.

## Prerequisites

Before running the code, ensure you have the following installed:

- `Python 3.7+`
- `gradio`
- `opencv-python`
- `numpy`
- `ultralytics`
- `supervision`

You can install the required packages using pip:

```bash
pip install gradio opencv-python numpy ultralytics supervision
```

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/NAEEM-UL-HASSAN/ML-Internship.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 26th-June
    ```

3. Open the provided Jupyter Notebook file (i.e Vehicle_Detection.ipynb) in the Jupyter interface.

4. Follow the instructions in the notebook to upload your video and run the vehicle detection code.

