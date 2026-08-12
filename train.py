import os
from ultralytics import YOLO
model=YOLO("yolov8n-seg.pt")
folder_path=r"C:\Users\abidli\Desktop\yolov8\choufli hall carcters segmentati.v5-please-work-wtf.yolov8"
file_name="data.yaml"
full_path=os.path.join(folder_path,file_name)
model.train(
    data=full_path
    ,epochs=70
    ,imgsz=640
    ,batch=16
    ,workers=0
)