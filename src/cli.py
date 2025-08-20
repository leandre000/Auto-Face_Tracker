import argparse
from src.face_tracker import FaceTracker

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--port")
    p.add_argument("--simulate", action="store_true")
    args=p.parse_args()
    if not args.simulate and not args.port: p.error("--port required")
    FaceTracker(args.port, args.simulate).start()

if __name__=="__main__": main()
