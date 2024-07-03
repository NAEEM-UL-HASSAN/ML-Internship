# MedSAM Segmentation Tool

This repository contains code for a segmentation tool that utilizes the MedSAM model to segment images based on bounding box coordinates. The application is built using Gradio for the user interface, allowing users to upload images, annotate bounding boxes, and view the segmentation results.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.6+
- PyTorch
- Gradio
- gradio-image-annotation
- NumPy
- Matplotlib
- scikit-image
- OpenCV
- segment-anything

## Description
The code includes the following main functionalities:

1. `Visualization Functions:` Functions to display masks and bounding boxes on images using Matplotlib.

2. `MedSAM Inference:` A function to perform inference using the MedSAM model, generating segmentation masks from image embeddings and bounding box coordinates.

3. `Segment Image:` A function to preprocess an input image, run it through the MedSAM model, and display the segmentation results alongside the original image with bounding boxes.

4. `Gradio Interface:` A Gradio-based user interface allowing users to upload images, annotate bounding boxes, and view the segmentation results.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/NAEEM-UL-HASSAN/ML-Internship.git
    ```

2. Open the 2nd-July Folder.

3. Upload `img_demo.png` inside your google drive `MyDrive` folder.

4. Download `medsam_vit_b.pth` from the below given link and upload it inside your google drive `MyDrive` folder.
    ```bash
    https://drive.google.com/drive/folders/1ETWmi4AiniJeWOt6HAsYgTjYv_fkgzoN
    ```

5. Now upload `medsam.ipynb` in Google Colab and run each cell


## Output

1. First click on `+` icon and then select the portion you want to segment and then click on `Get bounding boxes` button.

2. Now copy the coordinated and paste below the input field and click on `Segment Image` button.

3. Wait until image segment done. Now you can see the selected portion of image is segmented.

