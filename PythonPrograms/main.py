from utils.video_utils import read_video, save_video, detect_vehicles
from object_tracker.tracker import Tracker

def main():

    frames = read_video("C:\\Users\\pardh\\Infosys_STMS\\Data\\Video\\Traffic_01.mp4")

    # Video processing and detection
    detection_of_vehicles = detect_vehicles(frames)

    #object tracking
    obj_tracker = Tracker()
    result = obj_tracker.detect_objects(frames)

    output_frames = obj_tracker.draw_annotations(frames, result)


    save_video(frames, "C:\\Users\\pardh\\Infosys_STMS\\Output\\Output_01.avi")

if __name__ == '__main__':
    main()