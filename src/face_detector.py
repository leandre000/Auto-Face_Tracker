import cv2
import mediapipe as mp

class FaceDetector:
    def __init__(self, conf=0.5):
        self.mp_face=mp.solutions.face_detection
        self.detector=self.mp_face.FaceDetection(min_detection_confidence=conf)
    def detect(self, frame):
        rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results=self.detector.process(rgb)
        faces=[]
        if results.detections:
            for d in results.detections:
                bbox=d.location_data.relative_bounding_box
                h,w=frame.shape[:2]
                x=int(bbox.xmin*w)
                y=int(bbox.ymin*h)
                width=int(bbox.width*w)
                height=int(bbox.height*h)
                faces.append((x,y,width,height))
        return faces
    def close(self): self.detector.close()
