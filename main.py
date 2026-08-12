import cv2
import os
from ultralytics import YOLO
folder_path=r"C:\Users\abidli\Desktop\yolov8\runs\segment\train-9\weights"
file_name="best.pt"
full_path=os.path.join(folder_path,file_name)
model=YOLO(full_path)
try:
    video=cv2.VideoCapture(r"C:\Users\abidli\Desktop\yolov8\مسلسل شوفلي حل الموسم 2005 - الحلقة الثالثة.mp4")
    ret=True
    while ret:
        ret,frame=video.read()
        if not ret:
            break
        results=model.track(frame,persist=True,conf=0.6)
        annotated_frame=results[0].plot()
        cv2.putText(annotated_frame,"q: Quit",(20, 1060),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)
        cv2.imshow("Choufli_hall_caracter_detection",annotated_frame)
        if(cv2.waitKey(1) & 0XFF==ord("q")):
            break
except:
    image_error=cv2.imread("7158tA0bCNL.jpg")
    cv2.imshow("Choufli_hall_caracter_detection",image_error)

