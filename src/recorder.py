import cv2
class Recorder:
    def __init__(self, fname, fps=30, size=(640,480)):
        fourcc=cv2.VideoWriter_fourcc(*"XVID")
        self.writer=cv2.VideoWriter(fname, fourcc, fps, size)
    def write(self, frame): self.writer.write(frame)
    def release(self): self.writer.release()
