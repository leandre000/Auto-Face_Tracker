def calculate_center(bbox):
    x,y,w,h=bbox
    return (x+w//2, y+h//2)

def calculate_offset(center, frame_center):
    return center[0]-frame_center[0]

def is_in_dead_zone(offset, dz=50):
    return abs(offset)<dz

def calculate_steps(offset, mult=0.5, max_s=200):
    return min(int(abs(offset)*mult), max_s)
