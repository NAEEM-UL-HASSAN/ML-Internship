# YOLOv8 Object Detection API

This repository contains code for a FastAPI-based API that performs real-time object detection using YOLOv8 Small on uploaded images. It follows best practices for efficient and secure deployment, includes proper error handling, and provides detailed documentation for API endpoints.

## Task Description

The task involves creating a FastAPI application integrated with YOLOv8 Small for object detection on images. Key features of the API include:

1. Accepting image files as input for object detection.
2. Performing real-time object detection using YOLOv8 Small.
3. Handling different image file types (JPEG, PNG) and ensuring proper validation.
4. Implementing robust payload handling to manage file size limitations.
5. Providing a detailed summary of detected objects including object names, confidence scores, and bounding box coordinates.
6. Optimizing performance for concurrent requests and ensuring responsiveness.
7. Implementing proper error handling and clear error messages.
8. Documenting API endpoints thoroughly.

## Prerequisites

Before running the application, ensure you have the following installed:

- FastAPI
- Uvicorn
- OpenCV
- NumPy
- Ultralytics

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/NAEEM-UL-HASSAN/ML-Internship.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 12th-June
    ```

3. Install the required Python packages:
    ```bash
    pip install fastapi uvicorn opencv-python numpy ultralytics
    ```

4. Run this Command to upgrade the package:
    ```bash
    pip install --upgrade requests urllib3
    ```

## Usage

1. Run the script:
    ```bash
    uvicorn task:app --reload
    ```
2. Access the API at `http://127.0.0.1:8000` by typing this URL on Google URL bar and you will see the welcome message.

3. Now paste this URL `http://127.0.0.1:8000/docs` on Google URL bar.

4. Click on this `POST` button and then click on `Try it out` button.

5. Now choose the image file and click on `Execute` button.

6. You will see the detected object detail in Json format.


