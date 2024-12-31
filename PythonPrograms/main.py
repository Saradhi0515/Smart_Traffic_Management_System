from utils.video_utils import read_video, save_video, detect_vehicles
from object_tracker.tracker_3 import Tracker

def main():
    frames = read_video("X:\\Infosys_STMS\\Smart_Traffic_Management_System\\Data\\Video\\Traffic_05.mp4")

    track = Tracker()
    result = track.process_video(frames)

if __name__ == '__main__':
    main()

