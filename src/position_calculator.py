class PositionCalculator:
    def __init__(self, fw, fh, dz=50):
        self.fw=fw
        self.fh=fh
        self.dz=dz
        self.cx=fw//2
    def calculate_offset(self, bbox):
        x,y,w,h=bbox
        return (x+w//2)-self.cx
    def needs_adjustment(self, off):
        return abs(off)>self.dz
    def calculate_steps(self, off, m=0.5, ms=200):
        return min(int(abs(off)*m), ms)
    def get_direction(self, off):
        return "L" if off<0 else "R"
