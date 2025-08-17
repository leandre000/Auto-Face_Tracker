import serial
import time
from src.exceptions import SerialException

class SerialComm:
    def __init__(self, port, baud=115200, to=1.0):
        self.port=port
        self.baud=baud
        self.to=to
        self.ser=None
    def connect(self):
        self.ser=serial.Serial(self.port, self.baud, timeout=self.to)
        time.sleep(2)
    def send_command(self, cmd):
        if not self.ser or not self.ser.is_open: raise SerialException("Not open")
        self.ser.write(f"{cmd}\n".encode())
        return self.ser.readline().decode().strip()
    def close(self):
        if self.ser and self.ser.is_open: self.ser.close()
