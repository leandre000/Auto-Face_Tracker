import cv2
from src.exceptions import CameraException

class Camera:
    def __init__(self, idx=0, w=640, h=480):
        self.idx=idx
        self.w=w
        self.h=h
        self.cap=None
    def open(self):
        self.cap=cv2.VideoCapture(self.idx)
        if not self.cap.isOpened(): raise CameraException("Cannot open")
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.w)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.h)
    def read(self):
        ret,frame=self.cap.read()
        if not ret: raise CameraException("Read failed")
        return frame
    def release(self):
        if self.cap: self.cap.release()
