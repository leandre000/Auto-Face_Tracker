import cv2
from src.camera import Camera
from src.face_detector import FaceDetector
from src.position_calculator import PositionCalculator
from src.serial_comm import SerialComm
from src.simulator import Simulator
from src.config import Config

class FaceTracker:
    def __init__(self, port=None, sim=False):
        self.sim=sim
        self.camera=Camera(Config.CAMERA_INDEX, Config.FRAME_WIDTH, Config.FRAME_HEIGHT)
        self.detector=FaceDetector()
        self.calc=PositionCalculator(Config.FRAME_WIDTH, Config.FRAME_HEIGHT, Config.DEAD_ZONE)
        self.comm=Simulator() if sim else SerialComm(port, Config.BAUD_RATE)
        self.running=False
    def start(self):
        self.camera.open()
        self.comm.connect()
        self.running=True
        try:
            while self.running:
                frame=self.camera.read()
                faces=self.detector.detect(frame)
                if faces:
                    face=faces[0]
                    offset=self.calc.calculate_offset(face)
                    if self.calc.needs_adjustment(offset):
                        direction=self.calc.get_direction(offset)
                        steps=self.calc.calculate_steps(offset)
                        self.comm.send_command(f"{direction}{steps:03d}")
                    x,y,w,h=face
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imshow("Tracker",frame)
                if cv2.waitKey(1)&0xFF==ord("q"): break
        except KeyboardInterrupt: pass
        finally: self.stop()
    def stop(self):
        self.running=False
        self.camera.release()
        self.detector.close()
        self.comm.close()
        cv2.destroyAllWindows()
