# Choufli Hall Character Segmentation & Tracking YOLOv8

## Overview
This project focuses on detecting, segmenting, and tracking characters from the TV series "Choufli Hall" using a custom-trained YOLOv8 segmentation model. The model was trained on a small dataset and is designed to recognize multiple character classes in video scenes.

It combines:
- custom dataset preparation
- YOLOv8 segmentation training
- object tracking during video inference
- visual overlays for character detection

## Project Goal
The main goal is to detect and follow characters in video footage with segmentation and tracking, making it useful for visual analysis, monitoring, and future improvements in character recognition workflows.

## Version Info
- Version: 1.0
- Model type: YOLOv8 segmentation
- Dataset: small custom dataset
- Training status: prototype / experimental
- Classes: 8

## Tech Stack
- Python
- OpenCV
- Ultralytics YOLOv8
- PyTorch
- Roboflow
- Windows OS
- Computer vision pipeline

## Dataset
The project uses a custom dataset exported from Roboflow and stored in the following folder:

- `choufli hall carcters segmentati.v5-please-work-wtf.yolov8/`

Dataset configuration file:
- `data.yaml`

Detected character classes:
- AZZA
- Dalanda
- beji_matrix
- fouchika
- jannet
- sboui
- slimane
- zeineb

## Model Configuration
The model was trained using a YOLOv8 segmentation architecture with these settings:

- Base model: `yolov8n-seg.pt`
- Epochs: 70
- Image size: 640
- Batch size: 16
- Workers: 0
- Training script: `train.py`
- Best checkpoint: `best.pt`

## Project Structure
```text
choufli-hall-character-segmentation-tracking-yolov8/
├── best.pt
├── yolo26n.pt
├── yolov8n-seg.pt
├── main.py
├── train.py
├── readme.md
├── tempCodeRunnerFile.py
├── Failure image.jpg
├── مسلسل شوفلي حل الموسم 2005 - الحلقة الثالثة.mp4
├── runs/
│   └── segment/
│       ├── train/
│       ├── train-2/
│       ├── train-3/
│       ├── train-4/
│       ├── train-5/
│       ├── train-6/
│       ├── train-7/
│       ├── train-8/
│       ├── train-9/
│       └── ...
├── train/
├── choufli hall carcters segmentati.v5-please-work-wtf.yolov8/
│   ├── data.yaml
│   ├── README.dataset.txt
│   ├── README.roboflow.txt
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   └── test/
│       ├── images/
│       └── labels/
├── choufli hall carcters segmentati.v5-please-work-wtf.yolov8.zip
└── .gitignore
```

## File Descriptions
- `train.py` — trains the YOLOv8 segmentation model on the custom dataset.
- `main.py` — loads the trained model and runs inference on a video with tracking.
- `best.pt` — best trained model checkpoint.
- `yolov8n-seg.pt` — pretrained YOLOv8 segmentation weights.
- `runs/segment/...` — training metrics, logs, and experiment outputs.
- `data.yaml` — dataset metadata, class names, and path configuration.
- `Failure image.jpg` — fallback image used when video processing fails.

## Setup
1. Make sure Python 3.9+ is installed.
2. Install the required dependencies:

```bash
pip install ultralytics opencv-python torch
```

3. Prepare the dataset folder and ensure the path matches the project setup.
4. Run the training script:

```bash
python train.py
```

## Training
The training process is defined in `train.py` and is based on YOLOv8 segmentation:

```python
from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")
model.train(
    data="C:/path/to/choufli hall carcters segmentati.v5-please-work-wtf.yolov8/data.yaml",
    epochs=70,
    imgsz=640,
    batch=16,
    workers=0
)
```

## Inference & Tracking
Run the model on a video:

```bash
python main.py
```

This script:
- reads a video file
- applies the trained model
- tracks objects with `persist=True`
- uses a confidence threshold of `0.6`
- overlays segmentation results on each frame
- exits when the user presses `q`

## Notes
This is version 1.0 of the project and it was trained on a small custom dataset. It is a solid prototype for experimentation, model validation, and future improvements.

Possible next steps:
- expand the dataset
- improve annotation quality
- tune hyperparameters
- add more training epochs
- test with a larger or more robust YOLOv8 model version

## License
This project uses a custom dataset and YOLOv8-based workflow. Please check the Roboflow metadata and dataset license for any usage restrictions.

## Project Context
This project was developed for custom character segmentation and tracking using a small dataset and a YOLOv8 segmentation model.

---

Made with Python, OpenCV, and YOLOv8.
