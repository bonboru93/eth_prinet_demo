import serial
import threading

class BriReader(threading.Thread):
    def __init__(self):
        super().__init__()
        self.s = serial.Serial("/dev/ttyACM0", 9600)
        self.value = 0;
    def run(self):
        while True:
                self.value = int(self.s.readline())