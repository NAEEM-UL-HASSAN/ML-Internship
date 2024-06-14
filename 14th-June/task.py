'It is a FAST API application integrated with YOLOv8 Small object detection in images.'

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import uvicorn
import cv2
import numpy as np
from ultralytics import YOLO

app = FastAPI()

class DetectionResult(BaseModel):
    """
    Represents the detection result of an object.

    Attributes:
        object (str): The name of the detected object.
        confidence (float): The confidence score of the detection.
        bbox (list): The bounding box coordinates [xmin, ymin, xmax, ymax].
    """
    object: str
    confidence: float
    bbox: list

# Initialize YOLOv8 Small model
model = YOLO("yolov8s.pt")

@app.post("/detect_objects", response_model=list[DetectionResult])
async def detect_objects(file: UploadFile = File(...)):
    """
    Endpoint to detect objects in an uploaded image file.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        List[DetectionResult]: A list of detected objects with details.
    """
    try:
        # Validate file type
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail= 
            "Invalid image type. Only JPEG and PNG are supported.")
        # Read image file
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  
        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image data.")       
        # Perform object detection
        results = model(img, agnostic_nms=True)

        # Extract detection results
        detection_results = []
        for result in results:
            for box in result.boxes:
                xyxy = box.xyxy[0].tolist()  # Bounding box coordinates
                conf = box.conf[0].item()  # Confidence score
                cls = int(box.cls[0].item())  # Class ID
                detection_results.append(DetectionResult(
                    object=model.names[cls],
                    confidence=conf,
                    bbox=xyxy
                ))

        return detection_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    """
    Endpoint to display a welcome message.

    Returns:
        dict: A JSON response with a welcome message.
    """
    return {"message": "Welcome to the YOLOv8 Object Detection API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
