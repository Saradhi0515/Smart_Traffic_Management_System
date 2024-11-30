from utils.video_utils import read_video, save_video, detect_vehicles
from object_tracker.tracker import Tracker

def main():

    frames = read_video("C:\\Users\\pardh\\PycharmProjects\\Infosys_STMS\\Data\\Video\\traffic2.mp4")

    # Video processing and detection
    detection_of_vehicles = detect_vehicles(frames)

    #ojbject Tracker
    obj_tracker = Tracker()
    result = obj_tracker.detect_objects(frames)

    output_frames = obj_tracker.draw_annotations(frames, result)



    save_video(frames, "C:\\Users\\pardh\\PycharmProjects\\Infosys_STMS\\Outputs\\AVI\\output2.avi")

if __name__ == '__main__':
    main()